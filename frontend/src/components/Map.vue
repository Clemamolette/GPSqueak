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
    var path = [[46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053], [46.662258298353755, -0.401619127517053]];
    var i = 0;
    while (i < path.length) {
      console.log(path[i]);
      L.marker(path[i]).addTo(map);
      i++;
    }
  },
};
</script>

<style>
#map {
  height: 50em;
  width: 100em;
}
</style>


<!---->
