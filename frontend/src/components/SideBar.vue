<template>
    <div id="sidebar">
        <p> Running mice :</p>
        <div id="mice">
            <img 
                v-for="(image, index) in images" 
                :key="index" 
                :src="image" 
                alt="squeak icon" 
                class="squeak_icon"/>
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
    isMouseRunning(index: number): boolean {
      return index % 2 === 0;
    },
  },
});
</script>

<style>
    #sidebar {
        background-color: #757F83;
        width: 20em;
        height: 37em;
        align-self: center;
    }

    #mice {
        display: flex;
        flex-wrap: wrap;
        margin: 1em;
        justify-content: center;
    }

    .squeak_icon {
        width: 4em;
    }
</style>
