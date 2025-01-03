
"""
Latitude : 
degré entre la position et l'équateur
    nord (+) et sud (-)

Longitude :
degré entre la position et le prime meridian
    ouest (-) et est (+)

    
écriture DMS exemple : 77° 30' 29.9988" S 	164° 45' 15.0012" E
Pour passer de l'écriture DD à DMS : 
partie entière latitude = degrés
partie entière de la partie décimale de latitude * 60 = minutes
partie décimale des minutes * 60 = secondes
direction nord (N) si postitve et sud (S) si négative

même chose pour la ongitude mais avec les directions est (E) si positive et ouest (W) si négative

"""

import numpy as np
import json
import logging

LOG = logging.getLogger("PRODUCER")


"""  Global parameters """
MIN_LATITUDE = -90.
MAX_LATITUDE = 90.
MIN_LONGITUDE = -180.
MAX_LONGITUDE = 180.

""" coordinates of the area around Pougne-Hérisson (French city) """
ACTIVE_MIN_LATITUDE = 46.657240
ACTIVE_MAX_LATITUDE = 46.664955
ACTIVE_MIN_LONGITUDE = -0.408307
ACTIVE_MAX_LONGITUDE = -0.387321

class Coordinate:
    """ Defines one position """
    
    def __init__(self, latitude = 0., longitude = 0., ip= ""):
        """ initialisation """
        self.latitude = latitude
        self.longitude = longitude
        self.ip = ip
    
    def next_coordinate(self):
        """ Updates self coordinates after the target moved """
        delta_max = 0.0001 #max value to move around
        delta_min = 0.00005

        delta_latitude = np.random.uniform(delta_min, delta_max) * np.random.choice([-1,1])
        while not (in_perimeter(self.latitude + delta_latitude, self.longitude)):
            delta_latitude = np.random.uniform(delta_min, delta_max) * np.random.choice([-1,1])
        self.latitude += delta_latitude

        delta_longitude = np.random.uniform(delta_min, delta_max) * np.random.choice([-1,1])
        while not (in_perimeter(self.latitude, self.longitude + delta_longitude)):
            delta_longitude = np.random.uniform(delta_min, delta_max) * np.random.choice([-1,1])
        self.longitude += delta_longitude

    def copy(self):
        """ Returns a deep copy of self, not binded together """
        return Coordinate(self.latitude, self.longitude, self.ip)
    
    def next_point(self):
        """ Returns another Coordinate object with updated coordinates """
        c = self.copy()
        c.next_coordinate()
        return c
    
    """ Getters and setters """
    def set_latitude(self, latitude):
        if (MIN_LATITUDE < latitude) and (latitude < MIN_LATITUDE) and (type(latitude) == float):
            self.latitude = latitude
        else:
            LOG.error("Format ou valeur invalide, saisissez un flottant entre", MIN_LATITUDE, "et", MAX_LATITUDE)
    def get_latitude(self):
        return self.latitude
    def set_longitude(self, longitude):
        if (MIN_LONGITUDE < longitude) and (longitude < MAX_LONGITUDE) and (type(longitude) == float):
            self.longitude = longitude
        else:
            LOG.error("Format ou valeur invalide, saisissez un flottant entre", MIN_LONGITUDE, "et", MAX_LONGITUDE)
    def get_longitude(self):
        return self.longitude

    def to_string_dd(self):
        """ Return a string describing the coordinates in DD format """
        return "Latitude : " + str(self.latitude) + " , Longitude : " + str(self.longitude)
    
    def to_string_dms(self):
        """ Return a string describing the coordinates in DMS format"""
        
        def convert_to_dms(x):
            x = abs(x)
            degrees = int(x)
            minutes = int((x - degrees) * 60)
            seconds = round( ((x-degrees)*60 -minutes) * 60 , 2)
            return degrees, minutes, seconds

        degrees_lalitude, minutes_latitude, seconds_latitude = convert_to_dms(self.latitude)
        degrees_longitude, minutes_longitude, seconds_longitude = convert_to_dms(self.longitude)

        direction_latitude = "N" if self.latitude >= 0 else  "S"
        direction_longitude = "E" if self.longitude >= 0 else "W"

        latitude_dms = f"{degrees_lalitude}°{minutes_latitude}'{seconds_latitude}\" {direction_latitude}"
        longitude_dms = f"{degrees_longitude}°{minutes_longitude}'{seconds_longitude}\" {direction_longitude}"

        return str(latitude_dms) + " " + str(longitude_dms)


    def generate_coordinate(ip:str) -> 'Coordinate':
        """ Returns an randomly-initialized Coordinate object """
        latitude = np.random.uniform(ACTIVE_MIN_LATITUDE, ACTIVE_MAX_LATITUDE)
        longitude = np.random.uniform(ACTIVE_MIN_LONGITUDE, ACTIVE_MAX_LONGITUDE)
        return Coordinate(latitude, longitude,ip)
    
    def json(self) -> str:
        """Serialise coordinate to json"""
        dictionnary = {'ip': self.ip, 'latitude': self.latitude, 'longitude': self.longitude}
        return json.dumps(dictionnary).encode('utf-8')


def in_perimeter(latitude, longitude):
    """ Returns boolean value for if the position is within the defined perimeter """
    if (MIN_LATITUDE < latitude) and (latitude < MAX_LATITUDE) and (MIN_LONGITUDE < longitude) and (longitude < MAX_LONGITUDE):
        return True
    else:
        return False
    
if __name__ == "__main__":
    coords = [Coordinate.generate_coordinate("test")]
    for i in range(10):
        coords.append(coords[-1].next_point())

    x = [coords[i].get_latitude() for i in range(len(coords))]
    y = [coords[i].get_longitude() for i in range(len(coords))]

    points = []
    for i in range(len(x)):
        points.append([x[i], y[i]])
    print(points)