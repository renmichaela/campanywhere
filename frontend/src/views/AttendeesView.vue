<script setup>
import { computed, onMounted, ref, watch } from 'vue';
import ListItem from '../components/ListItem.vue';
import SupportIcon from '../components/icons/IconSupport.vue';

const attendees = ref([]);
const payments = ref([]);
const search = ref('');

onMounted(() => {
  fetch(`${import.meta.env.VITE_API_URL}/attendees`)
    .then(response => response.json())
    .then(data => {
      attendees.value = data.map(attendee => ({ ...attendee, showDetails: false }));
    });

  fetch(`${import.meta.env.VITE_API_URL}/payments`)
    .then(response => response.json())
    .then(data => payments.value = data);
});

const sortedAttendees = computed(() => {
  attendees.value.sort((a, b) => a.date - b.date);
  return attendees.value.filter(attendee => {
    return attendee.user.first_name.toLowerCase().includes(search.value.toLowerCase())
      || attendee.user.last_name.toLowerCase().includes(search.value.toLowerCase());
  });
});

const getTotalPaid = (attendeeId) => {
  const payment = payments.value.find(payment => payment.attendee_id === attendeeId);
  return payment ? Math.round(payment.total_paid * 100) / 100 : 0;
};

const getTotalOwed = (attendee) => {
  return Math.round((attendee.share_of_camping_expenses + attendee.share_of_paid_camping_expenses + attendee.share_of_electric_expenses + attendee.share_of_paid_electric_expenses) * 100) / 100;
};
</script>

<template>
  <main>
    <input type="text" placeholder="Search attendees" v-model="search" />
    <div class="attendee-cards">
      <div v-for="attendee in sortedAttendees" :key="attendee.id" class="attendee-card">
        <div class="card-header">
          <!-- <SupportIcon /> -->
          <div class="card-title">{{ attendee.user.first_name }} {{ attendee.user.last_name }}</div>
        </div>
        <div class="card-body">
          <p><strong>Camping Type:</strong> {{ attendee.camping_type.charAt(0) + attendee.camping_type.substring(1).toLowerCase() }}</p>
          <p><strong>Days Attending:</strong> {{ attendee.days_attending }} day{{ attendee.days_attending > 1 ? 's' : '' }}</p>
          <p><strong>Total Owed:</strong> ${{ getTotalOwed(attendee) }}</p>
          <p><strong>Total Paid:</strong> ${{ getTotalPaid(attendee.id) }}</p>
          <button @click="attendee.showDetails = !attendee.showDetails">
            {{ attendee.showDetails ? 'Hide Details' : 'Show Details' }}
          </button>
          <div v-if="attendee.showDetails" class="details">
            <p class="flex"><strong>Camping Cost Share:</strong> <span>{{ Math.round(attendee.camping_expense_share_weight * 100) }}%</span></p>
            <p class="flex"><strong>Owed for Paid Camping Expenses:</strong> <span>${{ attendee.share_of_paid_camping_expenses }}</span></p>
            <p class="flex"><strong>Owed for All Camping Expenses:</strong> <span>${{ attendee.share_of_camping_expenses }}</span></p>
            <p class="flex"><strong>Electric Cost Share:</strong> <span>{{ Math.round(attendee.electric_expense_share_weight * 100) }}%</span></p>
            <p class="flex"><strong>Owed for Paid Electric Expenses:</strong> <span>${{ attendee.share_of_electric_expenses }}</span></p>
            <p class="flex"><strong>Owed for All Electric Expenses:</strong> <span>${{ attendee.share_of_paid_electric_expenses }}</span></p>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
input {
  display: block;
  padding: 0.5rem;
  margin: 1.5rem auto;
  background-color: var(--input-bg, #fff);
  color: var(--input-color, #333);
}

.attendee-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.attendee-card {
  background: var(--color-background-mute);
  color: var(--color-text);
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  width: 90%;
}

.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.card-title {
  font-weight: bold;
}

.card-body p {
  margin: 0.5rem 0;
  font-size: 1rem;
  line-height: 1.5;
}

.card-body p.flex {
  display: flex;
  border-bottom: none;
  justify-content: space-between;
}

button {
  background: var(--color-green);
  color: var(--color-background-soft);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 0.5rem;
  font-weight: bold;
}

.details {
  margin-top: 1rem;
}

@media screen and (min-width: 640px) {
  .attendee-card {
    width: 70%;
  }
}

@media screen and (min-width: 1024px) {
  .attendee-card {
    width: 65%;
  }
}

@media screen and (min-width: 1280px) {
  .attendee-card {
    width: 50%;
  }
}

/* Dark mode styles */
@media (prefers-color-scheme: dark) {
  :root {
    --input-bg: #333;
    --input-color: #fff;
    --card-bg: #444;
    --card-color: #fff;
    --button-bg: #28a745;
    --button-hover-bg: #218838;
  }
}
</style>
