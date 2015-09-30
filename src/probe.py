# -*- coding: utf-8 -*-

# Constants to specify the quality of air status
# 
QAIR_STATUS_NOTPRESENT = -1 # Probe doesn't take measures on this pollutant
QAIR_STATUS_ERROR = 0       # Error on the measure taken
QAIR_STATUS_GOOD = 1
QAIR_STATUS_ACCEPTABLE = 2
QAIR_STATUS_BAD = 3
QAIR_STATUS_VERYBAD = 4

# Functions that return a a "quality of air" value depending on the 
# pollution parameter and the input value
#
# Have a look at the EU directives:
#   http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:32008L0050:EN:NOT
#
# Quality of air based on SO2 concentration
#   so2_value: raw string parsed from the HTML 
def qairStatus_SO2(so2_value):
    if (so2_value is None):
        return QAIR_STATUS_NOTPRESENT
    elif (so2_value == ""):
        return QAIR_STATUS_ERROR
    
    # thresholds taken from:
    #   http://www.miliarium.com/prontuario/Indices/IndiceCalidadAire.htm
    # quite similar to what can be seen here:
    #   http://www.troposfera.org/conceptos/la-legislacion-sobre-calidad-del-aire/conceptos-2/
    so2_value = float(so2_value)
    if (so2_value < 0):
        return QAIR_STATUS_ERROR
    elif (so2_value < 64):
        return QAIR_STATUS_GOOD
    elif (so2_value < 126):
        return QAIR_STATUS_ACCEPTABLE
    elif (so2_value < 187):
        return QAIR_STATUS_BAD
    else:
        return QAIR_STATUS_VERYBAD

# Quality of air based on O3 concentration
#   o3_value: raw string parsed from the HTML 
def qairStatus_O3(o3_value):
    if (o3_value is None):
        return QAIR_STATUS_NOTPRESENT
    elif (o3_value == ""):
        return QAIR_STATUS_ERROR
    
    # thresholds taken from:
    #   http://www.miliarium.com/prontuario/Indices/IndiceCalidadAire.htm
    # quite similar to what can be seen here:
    #   http://www.troposfera.org/conceptos/la-legislacion-sobre-calidad-del-aire/conceptos-2/
    o3_value = float(o3_value)
    if (o3_value < 0):
        return QAIR_STATUS_ERROR
    elif (o3_value < 60):
        return QAIR_STATUS_GOOD
    elif (o3_value < 120):
        return QAIR_STATUS_ACCEPTABLE
    elif (o3_value < 180):
        return QAIR_STATUS_BAD
    else:
        return QAIR_STATUS_VERYBAD

# Quality of air based on NO2 concentration
#   no2_value: raw string parsed from the HTML 
def qairStatus_NO2(no2_value):
    if (no2_value is None):
        return QAIR_STATUS_NOTPRESENT
    elif (no2_value == ""):
        return QAIR_STATUS_ERROR
    
    # thresholds taken from:
    #   http://www.miliarium.com/prontuario/Indices/IndiceCalidadAire.htm
    # quite similar to what can be seen here:
    #   http://www.troposfera.org/conceptos/la-legislacion-sobre-calidad-del-aire/conceptos-2/
    no2_value = float(no2_value)
    if (no2_value < 0):
        return QAIR_STATUS_ERROR
    elif (no2_value < 100):
        return QAIR_STATUS_GOOD
    elif (no2_value < 200):
        return QAIR_STATUS_ACCEPTABLE
    elif (no2_value < 300):
        return QAIR_STATUS_BAD
    else:
        return QAIR_STATUS_VERYBAD

# Quality of air based on PM10 concentration
#   pm10_value: raw string parsed from the HTML 
def qairStatus_PM10(pm10_value):
    if (pm10_value is None):
        return QAIR_STATUS_NOTPRESENT
    elif (pm10_value == ""):
        return QAIR_STATUS_ERROR
    
    # thresholds taken from:
    #     http://www.miliarium.com/prontuario/Indices/IndiceCalidadAire.htm
    # quite similar to what can be seen here:
    #   http://www.troposfera.org/conceptos/la-legislacion-sobre-calidad-del-aire/conceptos-2/
    pm10_value = float(pm10_value)
    if (pm10_value < 0):
        return QAIR_STATUS_ERROR
    elif (pm10_value < 25):
        return QAIR_STATUS_GOOD
    elif (pm10_value < 50):
        return QAIR_STATUS_ACCEPTABLE
    elif (pm10_value < 75):
        return QAIR_STATUS_BAD
    else:
        return QAIR_STATUS_VERYBAD
        
# Quality of air based on CO concentration
#   co_value: raw string parsed from the HTML 
def qairStatus_CO(co_value):
    if (co_value is None):
        return QAIR_STATUS_NOTPRESENT
    elif (co_value == ""):
        return QAIR_STATUS_ERROR
    
    # thresholds taken from:
    #   http://www.miliarium.com/prontuario/Indices/IndiceCalidadAire.htm
    # same thing seen here:
    #   taken from http://www.getafe.es/MAMBIENTE/delegacion/Cambio_Climatico/Calidad_del_Aire/Calidad_del_Aire.home
    #   http://www.troposfera.org/conceptos/la-legislacion-sobre-calidad-del-aire/conceptos-2/
    co_value = float(co_value)
    if (co_value < 0):
        return QAIR_STATUS_ERROR
    elif (co_value < 5):
        return QAIR_STATUS_GOOD
    elif (co_value < 10):
        return QAIR_STATUS_ACCEPTABLE
    elif (co_value < 15):
        return QAIR_STATUS_BAD
    else:
        return QAIR_STATUS_VERYBAD


class ProbeMeasure:
    """
        Contains all information regarding an atmospheric probe.
        It may also contain temeprature and other weather parameters
    """
    def __init__(self):
        # When was this measure taken?
        self.sample_time = None
        
        # pollution parameters
        self.co = None   # Carbon monoxide  - mg/m3. CO
        self.no = None   # Nitrix Oxide     - ug/m3. NO
        self.no2 = None  # Nitrogen dioxide - ug/m3. NO2
        self.so2 = None  # Sulfur dioxide - ug/m3. SO2
        self.pm25 = None # Particulate matter < 2.5 umeter - ug/m3. PM2.5
        self.pm10 = None # Particulate matter < 10 umeter  - ug/m3. PM10
        self.o3 = None   # Ozone   - ug/m3. O3
        self.sh2 = None  # Hydrogen sulfide - ug/m3. SH2
        self.tol = None  # Toluene - ug/m3. C6H5CH3
        self.ben = None  # Benzene - ug/m3. C6H6
        self.xyl = None  # Xylene  - ug/m3. C6H4(CH3)2
        
        # weather parameters
        self.wind_speed = None # Wind Speed     - m/s
        self.wind_dir = None   # Wind direction - degrees
        self.temp = None       # temperature    - celsius
        self.hum = None        # relative humidity - %
        self.pressure = None   # pressure        - mbar
        self.solar_rad = None  # solar radiation - W/m2
        self.precip = None     # precipitation  - liters/m2


class Probe:
    """
        Contains the description of a specific probe and a list of measures
    """
    def __init__(self, a_name, a_dataURL, a_latitude, a_longitude):
        self.name = a_name
        self.dataURL = a_dataURL
        self.latitude = a_latitude
        self.longitude = a_longitude
        
        self.last_measure = ProbeMeasure()
        #TODO handle old measures!!
        #self.old_measures = []
