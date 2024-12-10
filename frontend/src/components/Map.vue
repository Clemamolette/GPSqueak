<template>
  <div id="map"></div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import L from 'leaflet';
import { useMiceStore } from '../stores/mice';

type Coord = [number, number];

interface IconOptions extends L.IconOptions {
  shadowUrl: string;
  iconSize: [number, number];
  shadowSize: [number, number];
  iconAnchor: [number, number];
  shadowAnchor: [number, number];
  popupAnchor: [number, number];
  iconUrl: string
}

// Créer la classe SqueakIcon qui étend L.Icon
class SqueakIcon extends L.Icon {
  constructor(options: IconOptions) {
    super(options);
  }
}

const optionsDefault = {
    shadowUrl: '/squeak_icons/shadow_icon.png',
    iconSize: [35, 38],
    shadowSize: [40, 25],
    iconAnchor: [0, 20],
    shadowAnchor: [-5, 5],
    popupAnchor: [15, -25]
  }


function popup(coord: Coord): string {
  return `Coordonnées :\n${coord.toString()}`;
}

export default defineComponent({
  name: 'Map',
  mounted() {
    const miceStore = useMiceStore();
    const blueIcon = new SqueakIcon({...optionsDefault, iconUrl: miceStore.mouseBlue.src } as IconOptions);
    const blackIcon = new SqueakIcon({...optionsDefault, iconUrl: miceStore.mouseBlack.src}  as IconOptions);

    const map = L.map('map').setView([46.661326, -0.399094], 16);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

    const pathBlue = miceStore.mouseBlue.path;
    const pathBlack = miceStore.mouseBlack.path;

    const c1: Coord = [46.66351683019078, -0.4010184024809422];
    const c2: Coord = [46.661391638682026, -0.39771515366138493];

    miceStore.addCoordBlue(c1);
    miceStore.addCoordBlack(c2);

    L.polyline(pathBlue, { color: '#4b91bf', weight: 2, dashArray: '2, 5', dashOffset: 0 }as any).addTo(map);
    L.polyline(pathBlack, { color: '#696969', weight: 2, dashArray: '2, 5', dashOffset: 0 }as any).addTo(map);

    const lastPointBlue = pathBlue[pathBlue.length - 1];
    const lastPointBlack = pathBlack[pathBlack.length - 1];
    L.marker(lastPointBlue, { icon: blueIcon }).addTo(map).bindPopup(popup(lastPointBlue));
    L.marker(lastPointBlack, { icon: blackIcon }).addTo(map).bindPopup(popup(lastPointBlack));
  }
});
</script>

<style>
#map {
  height: 50em;
  width: 100em;
}
</style>
