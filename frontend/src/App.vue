<script setup lang="ts">
import 'leaflet/dist/leaflet.css';
import Map from './components/Map.vue'
import SideBar from './components/SideBar.vue'
</script>

<template>
  <div>
    <img src="/logo_gpsqueak.png" class="logo" alt="GPSqueak logo" />
  </div>
  <div id="app_bis">
    <SideBar></SideBar>
    <Map></Map>
  </div>
  
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

#app_bis {
  display: flex;
  flex-direction: row;
  gap: 5em;
}
</style>
