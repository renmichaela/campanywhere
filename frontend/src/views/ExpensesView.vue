<script setup>
import { computed, onMounted, ref, watch, reactive } from 'vue';
import ListItem from '../components/ListItem.vue';
import DocumentationIcon from '../components/icons/IconDocumentation.vue'

const expenses = ref([]);
const total_for_everyone = computed(() => expenses.value.filter(e => e.paid_by).reduce((acc, expense) => acc + parseFloat(expense.amount), 0));

onMounted(() => {
  fetch('http://localhost:8000/expenses')
    .then(response => response.json())
    .then(data => expenses.value = data);
});

const sortedExpenses = computed(() => expenses.value.sort((a, b) => a.date - b.date));
</script>

<template>
  <main>
    <ListItem v-for="expense in sortedExpenses" :key="expense.id">
      <template #icon>
        <DocumentationIcon />
      </template>
      <template #heading>{{ expense.name }}</template>
      <template #subheading>
        <span class="green">${{ expense.amount }}</span>
      </template>
      <div class="expense-details">
        <p>{{ new Date(expense.date.replace(/-/g, '\/')).toLocaleDateString('en-US') }}</p>
        <p v-if="expense.paid_by" class="expense-paid-by">Paid by: {{ expense.paid_by.user.first_name }}</p>
      </div>
      <p class="expense-description">{{ expense.description }}</p>
    </ListItem>
    <ListItem>
      <template #icon>
        <DocumentationIcon />
      </template>
      <template #heading>Totals</template>
      <div class="flex">
        <p>Expenses for everyone</p>
        <p class="green">${{ total_for_everyone }}</p>
      </div>
    </ListItem>
  </main>
</template>

<style scoped>
.expense-title {
  display: flex;
  justify-content: space-between;
}

.expense-details {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.expense-description {
  margin-bottom: 20px;
}

.expense-paid-by {
  font-size: 0.8rem;
  color: var(--color-text-light);
  text-align: right;
}
</style>