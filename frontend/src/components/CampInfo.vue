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
      <template #heading>Preregistration</template>

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
        <li>Starts 7am Saturday, Sept 7</li>
        <li>Arrive during assigned time slot</li>
        <li>Check in with WVF personel</li>
        <li>Put tarp(s) down in assigned row</li>
      </ul>
    </ListItem>
    <ListItem>
      <template #icon>
        <CommunityIcon />
      </template>
      <template #heading>Land Rush</template>

      <ul>
        <li>Starts 7am Thursday, Sept 12</li>
        <li>Arrive evening before and camp at our tarps from Line Up day</li>
        <li>Process into the campgrounds and claim our spot</li>
        <li>Typically purchase 1 or 2 more camping spots to account for the size of our space</li>
      </ul>
    </ListItem>
    <ListItem>
      <template #icon>
        <CommunityIcon />
      </template>
      <template #heading>Pre-Festival Weekend</template>

      <ul>
        <li>Many musicians and festival goers have moved in for the festival by this point</li>
        <li>No official stages; Low key, lots of tent jams</li>
        <li>You must have a Full Festival pass to attend</li>
      </ul>
    </ListItem>
    <ListItem>
      <template #icon>
        <CommunityIcon />
      </template>
      <template #heading>Walnut Valley Festival</template>

      <ul>
        <li>Festival officially starts Wednesday, Sept 18 and goes until Sunday, Sept 22</li>
        <li>Don't worry about where to camp, you can just Camp Anywhere!</li>
      </ul>
    </ListItem>
  </div>
</template>

<style scoped>
.crossed-off {
  text-decoration: line-through;
}
</style>