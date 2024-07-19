import { ref, computed } from 'vue'
import type { Ref } from 'vue'
import { defineStore } from 'pinia'

type User = {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
}

export const useUserStore = defineStore('user', () => {
  const users = ref({} as Record<number, User>);

  const addUser = (user: User) => {
    users.value[user.id] = user;
  }

  const getUser = (id: number): Ref<User> => {
    return computed(() => users.value[id]);
  }

  return { users, addUser, getUser };
});