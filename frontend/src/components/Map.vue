<template>
  <div id="map"></div>
</template>

<script>
import L from "leaflet";

var squeakIcon = L.Icon.extend({
    options: {
        shadowUrl: 'src/squeak_icons/shadow_icon.png',
        iconSize:     [35,38],
        shadowSize:   [40, 25],
        iconAnchor:   [0, 20],
        shadowAnchor: [-5, 5],
        popupAnchor:  [-3, -76]
    }
});
var blueIcon = new squeakIcon({iconUrl: 'src/squeak_icons/blue_icon.png'});



export default {
  mounted() {
    const map = L.map("map").setView([46.661326, -0.399094], 16);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);
    var path = [[46.66351683019078, -0.4010184024809422], [46.66356917576515, -0.40107429886611934], [46.66363765935244, -0.4011565986164805], [46.66370004697366, -0.40110653549862013], [46.66379760346246, -0.40117029956745365], [46.663882903134436, -0.4011000255296771], [46.663949308080205, -0.40115629708805756], [46.66404188803222, -0.4012367520283517], [46.66395897281155, -0.40131604821996786], [46.6638692452384, -0.40125223141246], [46.66394254808831, -0.40130582603688697]];
    var polyline = L.polyline(path, {color: '#4b91bf'}).addTo(map);
    var lastPoint = path[path.length - 1];
    var marker = L.marker(lastPoint, {icon: blueIcon}).addTo(map);
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
