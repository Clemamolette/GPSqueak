<template>
  <div id="map"></div>
</template>

<script>
import L from "leaflet";
import { useMiceStore } from "../stores/mice";

var squeakIcon = L.Icon.extend({
    options: {
        shadowUrl: '/squeak_icons/shadow_icon.png',
        iconSize:     [35,38],
        shadowSize:   [40, 25],
        iconAnchor:   [0, 20],
        shadowAnchor: [-5, 5],
        popupAnchor:  [15, -25]
    }
});

function popup(coord) {
  return "Coordonnées :\n" + coord.toString();
}

export default {
  mounted() {
    const miceStore = useMiceStore(); 
    const blueIcon = new squeakIcon({ iconUrl: miceStore.blueIcon }); 
    const blackIcon = new squeakIcon({ iconUrl: miceStore.blackIcon }); 

    const map = L.map("map").setView([46.661326, -0.399094], 16);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);y

    var pathBlue = miceStore.bluePath;
    var pathBlack = miceStore.blackPath;

    var polylineBlue = L.polyline(pathBlue, {color: '#4b91bf', weight: '2',  dashArray: '2, 5', dashOffset: '0'}).addTo(map);
    var polylineBlack = L.polyline(pathBlack, {color: '#696969', weight: '2',  dashArray: '2, 5', dashOffset: '0'}).addTo(map);

    var lastPointBlue = pathBlue[pathBlue.length - 1];
    var lastPointBlack = pathBlack[pathBlack.length - 1]; 
    var markerBlue = L.marker(lastPointBlue, {icon: blueIcon}).addTo(map).bindPopup(popup(lastPointBlue));
    var markerBlack = L.marker(lastPointBlack, {icon: blackIcon}).addTo(map).bindPopup(popup(lastPointBlack));
  }
};

</script>

<style>
#map {
  height: 50em;
  width: 100em;
}
</style>
