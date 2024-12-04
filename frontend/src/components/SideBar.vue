<template>
    <div id="sidebar">
        <p> Running mice :</p>
        <div id="mice">
            <img 
                v-for="(image, index) in images" 
                :key="index" 
                :src="image" 
                v-if="isMouseRunning(index)" 
                alt="squeak icon" 
                class="squeak_icon"/>
        </div>
    </div>
</template>

<script>
function running(index) {
    return true;
}


export default {
    data() {
        return {
            images: [],
        };
    },
    mounted() {
        this.images = [
            "/squeak_icons/black_icon.png",
            "/squeak_icons/blue_icon.png",
            "/squeak_icons/pink_icon.png",
            "/squeak_icons/red_icon.png",
        ];
    },
    methods: {
        isMouseRunning(index) {
            return index % 2 === 0; 
        },
    },
};
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
