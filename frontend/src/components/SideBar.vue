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
import { defineComponent, ref, onMounted, watch} from 'vue';
import { useMiceStore } from "../stores/mice";


export default defineComponent({
  name: 'MouseComponent',
  setup() {
      const miceStore = useMiceStore();
      const images = ref<string[]>([]);

      onMounted(() => {
        miceStore.mouses.forEach((value) => {
          images.value.push(value.src);
        });
      });
      
      watch(() => miceStore.mouses.length,
            (_new_length) => {
              miceStore.mouses.forEach((value) => {
                images.value.push(value.src);
              });
            }
      );

      const goToMouse = (index: number): void => {
        const coord = miceStore.getMouseCoord(index);
        if (coord) {
          miceStore.setView(coord);
        }
      };

      return {
        images,
        goToMouse,
      };
    },

  // data() {
  //   return {
  //     images: [] as string[], 
  //   };
  // },
  // mounted() {
  //   const miceStore = useMiceStore();
    
  //   miceStore.mouses.forEach((value) => {
  //     this.images.push(value.src);
  //   });

  // },
  // methods: {
  //   goToMouse(index: number): void {
  //     const miceStore = useMiceStore();
  //     const coord = miceStore.getMouseCoord(index);
  //     if (coord) {
  //       miceStore.setView(coord);
  //     }
  //   },
  // },
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
        height: 4em;
        filter: drop-shadow(0 0 1.2em #ffffff28);
        background-size: 100% 100%;

    }
    .squeak_icon:hover {
      filter: drop-shadow(0 0 1.2em #ffffffcb);
      cursor: pointer;
    }
</style>
