<script setup>
import ListItem from '../components/ListItem.vue';
import CommunityIcon from './icons/IconCommunity.vue'
</script>

<template>
  <div>
    <ListItem>
      <template #icon>
        <CommunityIcon />
      </template>
      <template #heading>Ticket Info</template>

      <ul>
        <li>Full Festival (Wed - Sat): $125 until Friday, Sept 13 ($150)</li>
        <li>Friday/Saturday: $110 until Friday, Sept 13 ($130)</li>
        <li>Fri or Sat only: $80 until Friday, Sept 13 ($90)</li>
      </ul>
    </ListItem>
    <ListItem>
      <template #icon>
        <CommunityIcon />
      </template>
      <template #heading>
        <span class="crossed-off">Preregistration</span>
      </template>

      <ul>
        <li>8am Monday, July 1</li>
        <li>Purchase first camping spot for festival</li>
        <li>This gets us our spot in line for Line Up day</li>
      </ul>
    </ListItem>
    <ListItem>
      <template #icon>
        <CommunityIcon />
      </template>
      <template #heading>Line Up day</template>

      <ul>
        <li></li>
      </ul>
    </ListItem>
  </div>
</template>

<style scoped>
.crossed-off {
  text-decoration: line-through;
}
</style>