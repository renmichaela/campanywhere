<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/expenses">Expenses</RouterLink>
      <RouterLink to="/attendees">Attendees</RouterLink>
    </nav>
      <RouterView name="Header" />
  </header>

  <RouterView />
</template>

<style>
header {
  line-height: 1.5;
  max-height: 100vh;
}

header aside p {
  font-size: 0.8rem;
  margin-bottom: 1rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: block;
  padding: 0.5rem 1rem;
}

@media (min-width: 1024px) {
  header {
    padding-right: calc(var(--section-gap) / 2);
  }

  header aside {
    text-align: right;
    padding: 1rem;
    padding-left: 2rem;
    margin-top: 1rem;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  nav {
    text-align: right;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
