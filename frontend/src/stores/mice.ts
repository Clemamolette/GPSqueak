import { defineStore } from 'pinia'

type Coord = [number, number];

export const useMiceStore = defineStore('mice', {
    state: () => ({
		mouseBlue: {src:"/squeak_icons/blue_icon.png", path:[]},
        mouseBlack: {src:"/squeak_icons/black_icon.png", path:[]} 
	}),
    actions: {
		addCoordBlue(coord: Coord ) {
            this.mouseBlue["path"].push(coord);
        },
		addCoordBlack(coord: Coord) {
            this.mouseBlack["path"].push(coord);
        },
	},
	getters: {
		blueIcon: (state) => {
			return state.mouseBlue["src"]
		},
        blackIcon: (state) => {
			return state.mouseBlack["src"]
		},
		bluePath: (state) => {
			return state.mouseBlue["path"]
		},
		blackPath: (state) => {
			return state.mouseBlack["path"]
		},
		blueLastCoord: (state) => {
			return state.mouseBlue["path"][-1]
		},
		blackLastCoord: (state) => {
			return state.mouseBlack["path"][-1]
		},
		
	}
})
