<script setup>
import { computed, onMounted, ref, watch } from 'vue';
import ListItem from '../components/ListItem.vue';
import SupportIcon from '../components/icons/IconSupport.vue'

const attendees = ref([]);

onMounted(() => {
  fetch('http://localhost:8000/attendees')
    .then(response => response.json())
    .then(data => attendees.value = data);
});

const sortedAttendees = computed(() => attendees.value.sort((a, b) => a.date - b.date));
</script>

<template>
  <main>
    <ListItem v-for="attendee in sortedAttendees" :key="attendee.id">
      <template #icon>
        <SupportIcon />
      </template>
      <template #heading>{{ attendee.user.first_name }} {{ attendee.user.last_name }}</template>
      <template #subheading>
        <p>
          <span class="green">{{ attendee.camping_type.charAt(0) + attendee.camping_type.substring(1).toLowerCase() }}</span> 
          camping for 
          <span class="green">{{ attendee.days_attending }}</span>
          day{{ attendee.days_attending > 1 ? 's' : '' }}
        </p>
      </template>
      <div class="flex">
        <p>Share of costs by # of days</p>
        <p class="green">{{ Math.round(attendee.expense_share_weight * 100) }}%</p>
      </div>
      <div class="flex">
        <p>Share of costs by camping type</p>
        <p class="green">{{ Math.round(attendee.electric_expense_share_weight * 100) }}%</p>
      </div>
      <div class="flex">
        <p>Share of paid expenses</p>
        <p class="green">${{ Math.round((attendee.share_of_paid_expenses + Number.EPSILON) * 100) / 100 }}</p>
      </div>
    </ListItem>
  </main>
</template>
