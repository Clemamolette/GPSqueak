import { defineStore } from 'pinia'
import type { Marker, Polyline } from 'leaflet';

type Coord = [number, number];

export interface Mouse {
	id: string;
	src: string;
	path: Coord[];
	isActive: boolean;
	marker: Marker | null;
	polyline: Polyline | null;
}


// Définir l'interface pour l'état global du store
interface State {
    mouseBlue: Mouse;
    mouseBlack: Mouse;
}

export const useMiceStore = defineStore('mice', {
    state: ():State => ({
		mouseBlue: {
			id: "blue",
			src: "/squeak_icons/blue_icon.png",
			path: [],
			isActive: true,
			marker: null,
			polyline: null
		},
		mouseBlack: {
			id: "black",
			src: "/squeak_icons/black_icon.png",
			path: [],
			isActive: true,
			marker: null,
			polyline: null
		}
	}),
    actions: {
		setMarker(color: 'blue' | 'black', marker: Marker) {
			if (color === 'blue') {
				this.mouseBlue.marker = marker;
			} else {
				this.mouseBlack.marker = marker;
			}
		},
		setPolyline(color: 'blue' | 'black', polyline: Polyline) {
			if (color === 'blue') {
				this.mouseBlue.polyline = polyline;
			} else {
				this.mouseBlack.polyline = polyline;
			}
		},
		addCoordBlue(coord: Coord) {
			this.mouseBlue.path.push(coord);
			if (this.mouseBlue.marker && this.mouseBlue.polyline) {
				this.mouseBlue.marker.setLatLng(coord);
				this.mouseBlue.polyline.setLatLngs(this.mouseBlue.path);
			}
		},
		addCoordBlack(coord: Coord) {
			this.mouseBlack.path.push(coord);
			if (this.mouseBlack.marker && this.mouseBlack.polyline) {
				this.mouseBlack.marker.setLatLng(coord);
				this.mouseBlack.polyline.setLatLngs(this.mouseBlack.path);
			}
		},
		clearPaths() {
			this.mouseBlue.path = [];
			this.mouseBlack.path = [];
			if (this.mouseBlue.polyline) this.mouseBlue.polyline.setLatLngs([]);
			if (this.mouseBlack.polyline) this.mouseBlack.polyline.setLatLngs([]);
		}
	},
	getters: {
		blueLastCoord: (state) => state.mouseBlue.path[state.mouseBlue.path.length - 1],
		blackLastCoord: (state) => state.mouseBlack.path[state.mouseBlack.path.length - 1],
		blueActive: (state) => state.mouseBlue.isActive,
		blackActive: (state) => state.mouseBlack.isActive
	}
})
