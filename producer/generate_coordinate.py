
"""
Latitude : 
degré entre la position et l'équateur
    nord (+) et sud (-)

Longitude :
degré entre la position et le prime meridian
    ouest (-) et est (+)

"""

import numpy as np


MIN_LATITUDE = 0.
MAX_LATITUDE = 90.
MIN_LONGITUDE = 0.
MAX_LONGITUDE = 180.

class Coordinate:
    def __init__(self, latitude = 0., longitude = 0.):

        self.latitude = latitude
        self.longitude = longitude
    

    def next_coordinate(self):

        # à faire de manière cohérente
        self.latitude += 1.
        self.longitude += 1.
    
    def toString(self):
        return "Latitude : " + str(self.latitude) + " , Longitude : " + str(self.longitude)



def generate_coordinate():
    latitude = np.random.uniform(MIN_LATITUDE, MAX_LATITUDE)
    longitude = np.random.uniform(MIN_LONGITUDE, MAX_LONGITUDE)
    coord = Coordinate(latitude, longitude)
    return coord


