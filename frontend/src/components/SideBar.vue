<template>
    <div id="sidebar">
        <p> Click to take a closer look</p>
        <div id="mice">
            <img 
                v-for="(image, index) in images" 
                :key="index" 
                :src="image" 
                alt="squeak icon" 
                class="squeak_icon"
                v-on:click="goToMouse(index)"
                />
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useMiceStore } from "../stores/mice";


export default defineComponent({
  name: 'MouseComponent',
  data() {
    return {
      images: [] as string[], 
    };
  },
  mounted() {
    const miceStore = useMiceStore();
    this.images = [
      miceStore.mouseBlue.src,
      miceStore.mouseBlack.src,
    ];
  },
  methods: {
    goToMouse(index: number): void {
      const miceStore = useMiceStore();
      const coord = index === 0 ? miceStore.blueLastCoord : miceStore.blackLastCoord;
      if (coord) {
        miceStore.setView(coord);
      }
    },
  },
});
</script>

<style>
    #sidebar {
        width: 20em;
        height: 20em;
        align-self: center;
    }

    #mice {
        display: flex;
        flex-wrap: wrap;
        margin: 1em;
        justify-content: center;
        gap: 2em;
    }

    .squeak_icon {
        width: 4em;
        filter: drop-shadow(0 0 1.2em #ffffff28);
    }
    .squeak_icon:hover {
      filter: drop-shadow(0 0 1.2em #ffffffcb);
      cursor: pointer;
    }
</style>
