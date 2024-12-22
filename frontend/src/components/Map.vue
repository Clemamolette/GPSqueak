<template>
  <div id="map"></div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import L from 'leaflet';
import { useMiceStore } from '../stores/mice';

type Coord = [number, number];

interface ComponentData {
  map: L.Map | null;
  updateInterval: number | null;
  apiBaseUrl: string;
}

// pour la définition des types et options par défaut de l'icon de souris
interface IconOptions extends L.IconOptions {
  shadowUrl: string;
  iconSize: [number, number];
  shadowSize: [number, number];
  iconAnchor: [number, number];
  shadowAnchor: [number, number];
  popupAnchor: [number, number];
  iconUrl: string
}
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
  data(): ComponentData {
    return {
      map: null,
      updateInterval: null,
      apiBaseUrl: 'http://localhost:8084'  // A CHANGER SI BESOIN
    };
  },
  mounted() {
    const miceStore = useMiceStore();
    const blueIcon = new SqueakIcon({...optionsDefault, iconUrl: miceStore.mouseBlue.src } as IconOptions);
    const blackIcon = new SqueakIcon({...optionsDefault, iconUrl: miceStore.mouseBlack.src}  as IconOptions);

    this.map = L.map("map").setView([46.661326, -0.399094], 16);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(this.map);

    // on initialise les chemins et les icons de souris
    const polylineBlue = L.polyline([], {
      color: '#4b91bf',
      weight: '2',
      dashArray: '2, 5',
      dashOffset: '0'
    }).addTo(this.map);
    const polylineBlack = L.polyline([], {
      color: '#696969',
      weight: '2',
      dashArray: '2, 5',
      dashOffset: '0'
    }).addTo(this.map);
    const markerBlue = L.marker([0, 0], {icon: blueIcon}).addTo(this.map);
    const markerBlack = L.marker([0, 0], {icon: blackIcon}).addTo(this.map);

    // puis on les garde dans le store
    miceStore.setMarker('blue', markerBlue);
    miceStore.setMarker('black', markerBlack);
    miceStore.setPolyline('blue', polylineBlue);
    miceStore.setPolyline('black', polylineBlack);

    // après toutes les initialisations : démarrage de la mise à jour périodique
    this.startUpdates();
  },
  beforeUnmount() {
    this.stopUpdates();
  },
  methods: {
    async fetchMousePosition(id: number) {
      try {
        // on va chercher l'api
        const response = await fetch(`${this.apiBaseUrl}/position/${id}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
      } catch (error) {
        console.error(`Erreur lors de la récupération de la position pour l'ID ${id}:`, error);
        return null;
      }
    },

    // mise à jour des positions des deux souris
    async updatePositions() {
      const miceStore = useMiceStore();
      try {
        const blueData = await this.fetchMousePosition(1);
        const blackData = await this.fetchMousePosition(2);

        console.log(blueData);
        console.log(blackData);
        
        // si on a bien de la donnée, on ajoute les coordonnées dans le store
        if (blueData.length > 0) {
          const blueCoord: [number, number] = blueData[0];
          miceStore.addCoordBlue(blueCoord);
        }
        if (blackData.length > 0) {
          const blackCoord: [number, number] = blackData[0];
          miceStore.addCoordBlack(blackCoord);
        }
      } catch (error) {
        console.error('Erreur lors de la mise à jour des positions:', error);
      }
    },

    // fonction pour mettre à jour les positions toutes les x seoncdes
    startUpdates() {
      this.updatePositions();
      this.updateInterval = window.setInterval(() => {
        this.updatePositions();
      }, 2000);
    },

    // arrêt des appels à l'api
    stopUpdates() {
      if (this.updateInterval !== null) {
        window.clearInterval(this.updateInterval);
        this.updateInterval = null;
      }
    }
  }
});
</script>

<style>
#map {
  height: 50em;
  width: 100em;
}
</style>
