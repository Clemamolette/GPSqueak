
"""
Latitude : 
degré entre la position et l'équateur
    nord (+) et sud (-)

Longitude :
degré entre la position et le prime meridian
    ouest (-) et est (+)

"""

import numpy as np

"""  Global parameters """
MIN_LATITUDE = -90.
MAX_LATITUDE = 90.
MIN_LONGITUDE = -180.
MAX_LONGITUDE = 180.

class Coordinate:
    """ initialisation """
    def __init__(self, latitude = 0., longitude = 0.):
        self.latitude = latitude
        self.longitude = longitude
    
    """ Returns the new coordinates after the target moved """
    def next_coordinate(self):
        # à faire de manière cohérente
        self.latitude += 1.
        self.longitude += 1.
    
    """ Return a string describing the coordinates """
    def to_string(self):
        return "Latitude : " + str(self.latitude) + " , Longitude : " + str(self.longitude)
    
    """ Getters and setters """
    def set_latitude(self, latitude):
        if (MIN_LATITUDE < latitude) and (latitude < MIN_LATITUDE) and (type(latitude) == float):
            self.latitude = latitude
        else:
            print("Format ou valeur invalide, saisissez un flottant entre", MIN_LATITUDE, "et", MAX_LATITUDE)
    def get_latitude(self):
        return self.latitude
    def set_longitude(self, longitude):
        if (MIN_LONGITUDE < longitude) and (longitude < MAX_LONGITUDE) and (type(longitude) == float):
            self.longitude = longitude
        else:
            print("Format ou valeur invalide, saisissez un flottant entre", MIN_LONGITUDE, "et", MAX_LONGITUDE)
    def get_longitude(self):
        return self.longitude


""" Returns an randomly-initialized Coordinate object """
def generate_coordinate():
    latitude = np.random.uniform(MIN_LATITUDE, MAX_LATITUDE)
    longitude = np.random.uniform(MIN_LONGITUDE, MAX_LONGITUDE)
    coord = Coordinate(latitude, longitude)
    return coord


