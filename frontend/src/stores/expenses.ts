import { computed, ref } from 'vue'
import type { Ref } from 'vue'
import { defineStore } from 'pinia'

type Expense = {
  id: number;
  name: string;
  amount: number;
  date: string;
  description: string;
  paid_by: number;
}

export const useExpensesStore = defineStore('expenses', () => {
  const expenses = ref({} as Record<number, Expense>);

  const addExpense = (expense: Expense) => {
    expenses.value[expense.id] = expense;
  }

  const getExpense = (id: number): Ref<Expense> => {
    return computed(() => expenses.value[id]);
  }

  return { expenses, addExpense, getExpense };
})