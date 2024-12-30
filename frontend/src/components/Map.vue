<template>
  <div id="map"></div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import L from 'leaflet';
import { Mouse, useMiceStore } from '../stores/mice';

type Coord = [number, number];

interface ComponentData {
  map?: L.Map;
  updateInterval?: number;
  images: string[];
  apiBaseUrl: string;
}


function popup(coord: Coord): string {
  return `Coordonnées :\n${coord.toString()}`;
}

export default defineComponent({
  name:"MapComponent",
  data(): ComponentData {
    return {
      map: undefined,
      images: ["icon_aquamarine.svg","icon_black.svg","icon_blue.svg","icon_blueviolet.svg","icon_chartreuse.svg","icon_green.svg","icon_pink.svg","icon_red.svg","icon_yellow.svg"],
      updateInterval: undefined,
      apiBaseUrl: 'http://localhost:8084'  // A CHANGER SI BESOIN
    };
  },
  mounted() {
    const miceStore = useMiceStore();
    
    this.map = L.map("map").setView([46.661326, -0.399094], 16);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(this.map as L.Map);

    miceStore.setMap(this.map as L.Map);

    this.startUpdates();
  },
  beforeUnmount() {
    this.stopUpdates();
  },
  methods: {
    fetchMousePosition(id: number) {
      return fetch(`${this.apiBaseUrl}/position/${id}`);
    },
    
    fetchMousesCall() {
      return fetch(`${this.apiBaseUrl}/id`);
    },

    // mise à jour des positions des deux souris
    updatePositions() {
      const miceStore = useMiceStore();
      const mouses = miceStore.mouses;

      mouses.forEach((mouse,index) => {
        this.fetchMousePosition(mouse.id)
        .then((res) => res.json())
        .then((value) => {
            if (value.length > 0) {
              let coord: [number, number] = value[0];
              miceStore.addCoord(index,coord);
            }
          })
        .catch((error) => {
          console.error('Erreur lors de la mise à jour des positions:', error);
        });
      });
    },

    fetchMouses() {
      const miceStore = useMiceStore();
      this.fetchMousesCall()
        .then((res) => res.json())
        .then((val) => {
          for(const [k,v] of Object.entries(val)) {


            if (miceStore.mouseExist(v as number)) {
              continue;
            }

            let img_src = "icon_black.svg";
            if (this.images.length>0) {
              let i = Math.floor(Math.random() * this.images.length);
              img_src = this.images[i]
              this.images.splice(i,1);
            }

            let mouse: Mouse = {
              id: v as number,
              name: k as string,
              src: '/squeak_icons/'+img_src,
              path: [],
              isActive: true
            }
            miceStore.addMouse(mouse);
          }
        }).catch((error) => {
          console.error('Erreur lors de la récupération des souris:', error);
        });

    },


    // fonction pour mettre à jour les positions toutes les x seoncdes
    async startUpdates() {
      this.fetchMouses();
      this.updatePositions();
      this.updateInterval = window.setInterval(async () => {
        this.fetchMouses();
        this.updatePositions();
      }, 2000);
    },

    // arrêt des appels à l'api
    stopUpdates() {
      if (this.updateInterval !== null) {
        window.clearInterval(this.updateInterval);
        this.updateInterval = undefined;
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
