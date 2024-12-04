<template>
  <div id="map"></div>
</template>

<script>
import L from "leaflet";

export default {
  mounted() {
    const map = L.map("map").setView([46.661326, -0.399094], 16);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);
  },
};
</script>

<style>
#map {
  height: 50em;
  width: 100em;
}
</style>


<!--[[46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635], [46.661398450802956, -0.3877881805170635]]-->
