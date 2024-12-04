<template>
  <div id="map"></div>
</template>

<script>
import L from "leaflet";

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
var blueIcon = new squeakIcon({iconUrl: '/squeak_icons/blue_icon.png'});
var blackIcon = new squeakIcon({iconUrl: '/squeak_icons/black_icon.png'});

function popup(coord) {
  return "Coordonnées :\n" + coord.toString();
}

export default {
  mounted() {
    const map = L.map("map").setView([46.661326, -0.399094], 16);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    var pathBlue = [[46.66351683019078, -0.4010184024809422], [46.66356917576515, -0.40107429886611934], [46.66363765935244, -0.4011565986164805], [46.66370004697366, -0.40110653549862013], [46.66379760346246, -0.40117029956745365], [46.663882903134436, -0.4011000255296771], [46.663949308080205, -0.40115629708805756], [46.66404188803222, -0.4012367520283517], [46.66395897281155, -0.40131604821996786], [46.6638692452384, -0.40125223141246], [46.66394254808831, -0.40130582603688697]];
    var pathBlack = [[46.661391638682026, -0.39771515366138493], [46.66130614408653, -0.39764117619061884], [46.661236674245245, -0.3977405814935302], [46.66128755215628, -0.3976684287259818], [46.661189747719945, -0.3977616991966276], [46.66128431200816, -0.39768675090991185], [46.66133897303489, -0.39761064841047966], [46.66139143114053, -0.397559611706186], [46.661443364657025, -0.3974865905370269], [46.66137724155712, -0.39757444438099604], [46.661441577021385, -0.3975185495724689]];

    var polylineBlue = L.polyline(pathBlue, {color: '#4b91bf', weight: '2',  dashArray: '2, 5', dashOffset: '0'}).addTo(map);
    var polylineBlack = L.polyline(pathBlack, {color: '#696969', weight: '2',  dashArray: '2, 5', dashOffset: '0'}).addTo(map);

    var lastPointBlue = pathBlue[pathBlue.length - 1];
    var lastPointBlack = pathBlack[pathBlack.length - 1]; 
    var markerBlue = L.marker(lastPointBlue, {icon: blueIcon}).addTo(map).bindPopup(popup(lastPointBlue));
    var markerBlack = L.marker(lastPointBlack, {icon: blackIcon}).addTo(map).bindPopup(popup(lastPointBlack));
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
