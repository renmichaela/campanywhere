<script setup>
import { computed, onMounted, ref, watch } from 'vue';
import ListItem from '../components/ListItem.vue';
import SupportIcon from '../components/icons/IconSupport.vue';

const attendees = ref([]);
const search = ref('');

onMounted(() => {
  fetch(`${import.meta.env.VITE_API_URL}/attendees`)
    .then(response => response.json())
    .then(data => attendees.value = data);
});

const sortedAttendees = computed(() => {
  attendees.value.sort((a, b) => a.date - b.date)
  return attendees.value.filter(attendee => {
    return attendee.user.first_name.toLowerCase().includes(search.value.toLowerCase())
      || attendee.user.last_name.toLowerCase().includes(search.value.toLowerCase());
  })
});
</script>

<template>
  <main>
    <input type="text" placeholder="Search attendees" v-model="search" />
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
        <p>Share of camping costs by # of days</p>
        <p>{{ Math.round(attendee.camping_expense_share_weight * 100) }}%</p>
      </div>
      <div class="flex">
        <p>Owed for paid camping expenses</p>
        <p class="green">${{ attendee.share_of_paid_camping_expenses }}</p>
      </div>
      <div class="flex">
        <p>Owed for all camping expenses</p>
        <p>${{ attendee.share_of_camping_expenses }}</p>
      </div>
      <div class="flex">
        <p>Share of electric costs by camping type</p>
        <p>{{ Math.round(attendee.electric_expense_share_weight * 100) }}%</p>
      </div>
      <div class="flex">
        <p>Owed for paid electric expenses</p>
        <p class="green">${{ attendee.share_of_electric_expenses }}</p>
      </div>
      <div class="flex">
        <p>Owed for all electric expenses</p>
        <p>${{ attendee.share_of_paid_electric_expenses }}</p>
      </div>
    </ListItem>
  </main>
</template>

<style scoped>
input {
  display: block;
  padding: 0.5rem;
  margin: 1.5rem auto;
}
</style>
