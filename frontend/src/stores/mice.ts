import { defineStore } from 'pinia'

type Coord = [number, number];

export const useMiceStore = defineStore('mice', {
    state: () => ({
		mouseBlue: {id:"blue", src:"/squeak_icons/blue_icon.png", path:[], isActive: true},
        mouseBlack: {id:"black", src:"/squeak_icons/black_icon.png", path:[], isActive: true} 
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
		blue: (state) => {
			return state.mouseBlue
		},
		black: (state) => {
			return state.mouseBlack
		},
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
		blueActive: (state) => {
			return state.mouseBlue["isActive"]
		},
		blackActive: (state) => {
			return state.mouseBlack["isActive"]
		},
		
	}
})
