<script setup lang="ts">
import 'leaflet/dist/leaflet.css';
import Map from './components/Map.vue'
</script>

<template>
  <div>
    <img src="./logo_gpsqueak.png" class="logo" alt="GPSqueak logo" />
  </div>
  <Map></Map>
</template>

<style scoped>
.logo {
  height: 12em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #eb8d0049);
}
</style>
