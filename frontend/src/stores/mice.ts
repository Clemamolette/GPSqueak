import { defineStore } from 'pinia'
import type { Marker, Polyline } from 'leaflet';
import L from 'leaflet';

type Coord = [number, number];

export interface Mouse {
	id: number;
	name: string;
	src: string;
	path: Coord[];
	isActive: boolean;
	marker?: Marker;
	polyline?: Polyline;
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


// Définir l'interface pour l'état global du store
interface State {
    // mouseBlue: Mouse;
    // mouseBlack: Mouse;
	mouses: Mouse[];
	map?: L.Map;
}


export const useMiceStore = defineStore('mice', {
	state: (): State => ({
		mouses: [],
		map: undefined,
	}),
	actions: {
		addMouse(mouse: Mouse) {
			
			if (!mouse.marker) {
				const icon = new SqueakIcon({...optionsDefault, iconUrl: mouse.src } as IconOptions);

				const marker = L.marker([0, 0], {icon: icon}).addTo(this.map as L.Map);
				mouse.marker = marker
			}
			
			if (!mouse.polyline) {
				const polyline = L.polyline([], {
				color: mouse.src.match(/.*\/icon_(.+)\.svg/)?.[1],
				weight: 2,
				dashArray: '2, 5',
				dashOffset: '0'
				}).addTo(this.map as L.Map);
				
				mouse.polyline = polyline;
			}
			
			this.mouses.push(mouse);
		},
		setMap(map: L.Map) {
			this.map = map;
		},
		setView(coord: Coord) {
            if (this.map) {
                this.map.setView(coord, 20);
            }
        },
		addCoord(index: number,coord: Coord) {
			if (index >= 0 && index < this.mouses.length) {
				this.mouses[index].path.push(coord);
				this.mouses[index].marker?.setLatLng(coord);
				this.mouses[index].polyline?.setLatLngs(this.mouses[index].path);

				if (this.mouses[index].path.length > 35) {
					this.mouses[index].path.splice(0,this.mouses[index].path.length - 35)
				}
			}
		},
		clearPaths() {
			this.mouses = this.mouses.map((value) => {
				value.path = [];
				value.polyline?.setLatLngs([]);
				return value;
			});
		},
		mouseExist(id: number) : boolean {
			return this.mouses.some((m) => m.id === id);
		},
	},
	getters: {
		getMouseCoord: (state) => (i: number) => state.mouses[i].path[state.mouses[i].path.length -1],
		getMouseActive: (state) => (i: number) => state.mouses[i].isActive,
		getMouses: (state) => state.mouses,
	},
});

		// mouseBlue: {
		// 	id: 1,
		// 	src: "/squeak_icons/blue_icon.png",
		// 	path: [],
		// 	isActive: true,
		// 	marker: null,
		// 	polyline: null
		// },
		// mouseBlack: {
		// 	id: 2,
		// 	src: "/squeak_icons/black_icon.png",
		// 	path: [],
		// 	isActive: true,
		// 	marker: null,
		// 	polyline: null
		// },