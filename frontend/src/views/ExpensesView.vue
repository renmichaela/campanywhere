<script setup>
import { computed, onMounted, ref, watch, reactive } from 'vue';
import ListItem from '../components/ListItem.vue';
import DocumentationIcon from '../components/icons/IconDocumentation.vue'

const expenses = ref([]);
const camping_expenses_paid = computed(() => expenses.value.filter(e => e.paid_by && e.type == "CAMPING").reduce((acc, expense) => acc + parseFloat(expense.amount), 0));
const camping_expenses_unpaid = computed(() => expenses.value.filter(e => !e.paid_by && e.type == "CAMPING").reduce((acc, expense) => acc + parseFloat(expense.amount), 0));
const total_camping_expenses = computed(() => expenses.value.filter(e => e.type == "CAMPING").reduce((acc, expense) => acc + parseFloat(expense.amount), 0));
const electric_expenses_paid = computed(() => expenses.value.filter(e => e.paid_by && e.type == "ELECTRIC").reduce((acc, expense) => acc + parseFloat(expense.amount), 0));
const electric_expenses_unpaid = computed(() => expenses.value.filter(e => !e.paid_by && e.type == "ELECTRIC").reduce((acc, expense) => acc + parseFloat(expense.amount), 0));
const total_electric_expenses = computed(() => expenses.value.filter(e => e.type == "ELECTRIC").reduce((acc, expense) => acc + parseFloat(expense.amount), 0));

onMounted(() => {
  fetch(`${import.meta.env.VITE_API_URL}/expenses`)
    .then(response => response.json())
    .then(data => expenses.value = data);
});

const sortedExpenses = computed(() => expenses.value.sort((a, b) => a.date - b.date));
</script>

<template>
  <main>
    <ListItem>
      <template #icon>
        <DocumentationIcon />
      </template>
      <template #heading>Totals</template>
      <div class="flex">
        <p>Camping Expenses (paid)</p>
        <p>${{ camping_expenses_paid }}</p>
      </div>
      <div class="flex">
        <p>...(unpaid)</p>
        <p>${{ camping_expenses_unpaid }}</p>
      </div>
      <div class="flex">
        <p class="green">Camping Expenses (total)</p>
        <p class="green">${{ total_camping_expenses }}</p>
      </div>
      <div class="flex">
        <p>Electric Expenses (paid)</p>
        <p>${{ electric_expenses_paid }}</p>
      </div>
      <div class="flex">
        <p>...(unpaid)</p>
        <p>${{ electric_expenses_unpaid }}</p>
      </div>
      <div class="flex">
        <p class="green">Electric Expenses (total)</p>
        <p class="green">${{ total_electric_expenses }}</p>
      </div>
    </ListItem>
    <ListItem v-for="expense in sortedExpenses" :key="expense.id" :item-details-style="{borderBottomStyle: 'dotted', borderBottomWidth: '2px'}">
      <template #icon>
        <DocumentationIcon />
      </template>
      <template #heading>
        <div class="expense-heading">
          {{ expense.name }}
          <span class="camping-type">{{ expense.type_label }}</span>
        </div>
      </template>
      <template #subheading>
        <span class="green">${{ expense.amount }}</span>
      </template>
      <div class="expense-details">
        <p>{{ new Date(expense.date.replace(/-/g, '\/')).toLocaleDateString('en-US') }}</p>
        <p v-if="expense.paid_by" class="expense-paid-by">Paid by: {{ expense.paid_by.user.first_name }}</p>
      </div>
      <p class="expense-description">{{ expense.description }}</p>
    </ListItem>
  </main>
</template>

<style scoped>
.expense-title {
  display: flex;
  justify-content: space-between;
}

.expense-heading {
  display: flex;
  align-items: center;
}

.expense-heading .camping-type {
  font-size: 0.6rem;
  background-color: var(--color-green);
  color: #000;
  font-weight: bold;
  padding: 0.2rem 0.5rem;
  border-radius: 0.5rem;
  margin-left: 0.5rem
}

.expense-details {
  display: flex;
  justify-content: space-between;
}

.expense-paid-by {
  font-size: 0.8rem;
  color: var(--color-text-light);
  text-align: right;
}
</style>