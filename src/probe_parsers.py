import urllib2
from HTMLParser import HTMLParseError

from html_parsers import MadridDotOrgHTMLParser
from html_parsers import MunimadridDotEsHTMLParser
from html_parsers import TresCantosDotEsHTMLParser
from html_parsers import JCCMDotEsHTMLParser
from html_parsers import AirecantabriaHTMLParser
from html_parsers import AragonaireHTMLParser

from probe import ProbeMeasure
from probe import Probe

from constants import *

HTTP_HEADERS = {
    'Accept-Language': 'es-ES,es;q=0.8,en;q=0.5' }


class ProbeParser():
    """
        Virtual class to be inherited by all probe-parsing classes
        
        A probe-parsing class has a list of Probes that get updated
        by the "update" method (which is pure virtual). 
        
        This list of probes is a public attribute called "probe_list" that
        is instantiated in this class
    """
    
    def __init__(self):
        self.probe_list = list() # empty list
    
    @property
    def update(self):
        raise NotImplementedError("Subclasses should implement this!")


class MadridDotOrgLiveProbeParser(ProbeParser):
    """
        Parser to retrieve probe data from madrid.org
        
        Each probe has a specific data URL which will be used
        to download the HTML content and parse the live probe feed
    """
    def __init__(self):
        ProbeParser.__init__(self)
        # the HTML parser info
        self.__html_parser = MadridDotOrgHTMLParser()
        
        # fill up the probe list
        #
        # madrid.org 02 Corredor del henares
        self.probe_list.append(
            Probe(u'Alcalá de Henares', MADRID_DOT_ORG_PROBE_ALCALA_URL,
                MADRID_DOT_ORG_PROBE_ALCALA_LAT, MADRID_DOT_ORG_PROBE_ALCALA_LON))
        self.probe_list.append(
            Probe(u'Alcobendas', MADRID_DOT_ORG_PROBE_ALCOBENDAS_URL,
                MADRID_DOT_ORG_PROBE_ALCOBENDAS_LAT, MADRID_DOT_ORG_PROBE_ALCOBENDAS_LON))
        self.probe_list.append(
            Probe(u'Torrejón de Ardoz', MADRID_DOT_ORG_PROBE_TORREJON_URL,
                MADRID_DOT_ORG_PROBE_TORREJON_LAT, MADRID_DOT_ORG_PROBE_TORREJON_LON))
        self.probe_list.append(
            Probe(u'Coslada', MADRID_DOT_ORG_PROBE_COSLADA_URL,
                MADRID_DOT_ORG_PROBE_COSLADA_LAT, MADRID_DOT_ORG_PROBE_COSLADA_LON))
        self.probe_list.append(
            Probe(u'Arganda del Rey', MADRID_DOT_ORG_PROBE_ARGANDA_URL,
                MADRID_DOT_ORG_PROBE_ARGANDA_LAT, MADRID_DOT_ORG_PROBE_ARGANDA_LON))
        self.probe_list.append(
            Probe(u'Rivas Vaciamadrid', MADRID_DOT_ORG_PROBE_RIVAS_URL,
                MADRID_DOT_ORG_PROBE_RIVAS_LAT, MADRID_DOT_ORG_PROBE_RIVAS_LON))
        self.probe_list.append(
            Probe(u'Algete', MADRID_DOT_ORG_PROBE_ALGETE_URL,
                MADRID_DOT_ORG_PROBE_ALGETE_LAT, MADRID_DOT_ORG_PROBE_ALGETE_LON))
        # madrid.org 03 Urbana sur
        self.probe_list.append(
            Probe(u'Getafe', MADRID_DOT_ORG_PROBE_GETAFE_URL,
                MADRID_DOT_ORG_PROBE_GETAFE_LAT, MADRID_DOT_ORG_PROBE_GETAFE_LON))
        self.probe_list.append(
            Probe(u'Leganés', MADRID_DOT_ORG_PROBE_LEGANES_URL,
                MADRID_DOT_ORG_PROBE_LEGANES_LAT, MADRID_DOT_ORG_PROBE_LEGANES_LON))
        self.probe_list.append(
            Probe(u'Fuenlabrada', MADRID_DOT_ORG_PROBE_FUENLABRADA_URL,
                MADRID_DOT_ORG_PROBE_FUENLABRADA_LAT, MADRID_DOT_ORG_PROBE_FUENLABRADA_LON))
        self.probe_list.append(
            Probe(u'Móstoles', MADRID_DOT_ORG_PROBE_MOSTOLES_URL,
                MADRID_DOT_ORG_PROBE_MOSTOLES_LAT, MADRID_DOT_ORG_PROBE_MOSTOLES_LON))
        self.probe_list.append(
            Probe(u'Alcorcón', MADRID_DOT_ORG_PROBE_ALCORCON_URL,
                MADRID_DOT_ORG_PROBE_ALCORCON_LAT, MADRID_DOT_ORG_PROBE_ALCORCON_LON))
        self.probe_list.append(
            Probe(u'Aranjuez', MADRID_DOT_ORG_PROBE_ARANJUEZ_URL,
                MADRID_DOT_ORG_PROBE_ARANJUEZ_LAT, MADRID_DOT_ORG_PROBE_ARANJUEZ_LON))
        self.probe_list.append(
            Probe(u'Valdemoro', MADRID_DOT_ORG_PROBE_VALDEMORO_URL,
                MADRID_DOT_ORG_PROBE_VALDEMORO_LAT, MADRID_DOT_ORG_PROBE_VALDEMORO_LON))
        # madrid.org 04 Urbana noroeste
        self.probe_list.append(
            Probe(u'Colmenar Viejo', MADRID_DOT_ORG_PROBE_COLMENAR_URL,
                MADRID_DOT_ORG_PROBE_COLMENAR_LAT, MADRID_DOT_ORG_PROBE_COLMENAR_LON))
        self.probe_list.append(
            Probe(u'Majadahonda', MADRID_DOT_ORG_PROBE_MAJADAHONDA_URL,
                MADRID_DOT_ORG_PROBE_MAJADAHONDA_LAT, MADRID_DOT_ORG_PROBE_MAJADAHONDA_LON))
        self.probe_list.append(
            Probe(u'Collado Villalba', MADRID_DOT_ORG_PROBE_COLLADO_URL,
                MADRID_DOT_ORG_PROBE_COLLADO_LAT, MADRID_DOT_ORG_PROBE_COLLADO_LON))
        # madrid.org 05 Rural sierra norte
        self.probe_list.append(
            Probe(u'Guadalix de la Sierra', MADRID_DOT_ORG_PROBE_GUADALIX_URL,
                MADRID_DOT_ORG_PROBE_GUADALIX_LAT, MADRID_DOT_ORG_PROBE_GUADALIX_LON))
        self.probe_list.append(
            Probe(u'El Atazar', MADRID_DOT_ORG_PROBE_ATAZAR_URL,
                MADRID_DOT_ORG_PROBE_ATAZAR_LAT, MADRID_DOT_ORG_PROBE_ATAZAR_LON))
        # madrid.org 06 Cuenca del Alberche
        self.probe_list.append(
            Probe(u'San Martín de Valdeiglesias', MADRID_DOT_ORG_PROBE_SANMARTIN_URL,
                MADRID_DOT_ORG_PROBE_SANMARTIN_LAT, MADRID_DOT_ORG_PROBE_SANMARTIN_LON))
        self.probe_list.append(
            Probe(u'Villa del Prado', MADRID_DOT_ORG_PROBE_ELPRADO_URL,
                MADRID_DOT_ORG_PROBE_ELPRADO_LAT, MADRID_DOT_ORG_PROBE_ELPRADO_LON))
        # madrid.org 07 Cuenca del tajuna
        self.probe_list.append(
            Probe(u'Villarejo de Salvanés', MADRID_DOT_ORG_PROBE_VILLAREJO_URL,
                MADRID_DOT_ORG_PROBE_VILLAREJO_LAT, MADRID_DOT_ORG_PROBE_VILLAREJO_LON))
        self.probe_list.append(
            Probe(u'Orusco de Tajuña', MADRID_DOT_ORG_PROBE_ORUSCO_URL,
                MADRID_DOT_ORG_PROBE_ORUSCO_LAT, MADRID_DOT_ORG_PROBE_ORUSCO_LON))
    
    def update(self):
        for thisProbe in self.probe_list:
            print "parsing madrid.org - " + thisProbe.name + "..."
            # ensure the parser is clean to start the parsing process
            self.__html_parser.reset()

            req = urllib2.Request(thisProbe.dataURL, data=None, headers=HTTP_HEADERS)
            htmlFile = urllib2.urlopen(req)
            
            # what character encoding set is this file????
            charset = htmlFile.headers.getparam('charset')
            
            for line in htmlFile.readlines():
                # gestiona.madrid.org is ISO-8859-1, but still we should be doing
                # things right
                line = line.strip().decode(charset).encode("utf-8")
                
                try:
                    self.__html_parser.feed(line)
                except HTMLParseError, ex:
                    print "Exception %s" % (ex.msg)
            
            htmlFile.close()
            
            # Are we parsing the correct station?
            # WARNING: 
            #   To get the unicode from the bytes, you decode. To get the bytes from unicode, you encode
            if (self.__html_parser.m_stationName.decode("utf-8") == thisProbe.name):            
                thisMeasure = ProbeMeasure()
                thisMeasure.sample_time = self.__html_parser.m_sampleTime
                
                if ('CO' in self.__html_parser.m_pollutants):
                    thisMeasure.co = self.__html_parser.m_pollutants['CO']
                if ('NO' in self.__html_parser.m_pollutants):
                    thisMeasure.no = self.__html_parser.m_pollutants['NO']
                if ('NO2' in self.__html_parser.m_pollutants):
                    thisMeasure.no2 = self.__html_parser.m_pollutants['NO2']
                if ('SO2' in self.__html_parser.m_pollutants):
                    thisMeasure.so2 = self.__html_parser.m_pollutants['SO2']
                if ('PM2,5' in self.__html_parser.m_pollutants):
                    thisMeasure.pm25 = self.__html_parser.m_pollutants['PM2,5']
                if ('PM10' in self.__html_parser.m_pollutants):
                    thisMeasure.pm10 = self.__html_parser.m_pollutants['PM10']
                if ('O3' in self.__html_parser.m_pollutants):
                    thisMeasure.o3 = self.__html_parser.m_pollutants['O3']
                if ('TOL' in self.__html_parser.m_pollutants):
                    thisMeasure.tol = self.__html_parser.m_pollutants['TOL']
                if ('BEN' in self.__html_parser.m_pollutants):
                    thisMeasure.ben = self.__html_parser.m_pollutants['BEN']
                if ('XIL' in self.__html_parser.m_pollutants):
                    thisMeasure.xyl = self.__html_parser.m_pollutants['XIL']
                
                if ('Velocidad viento' in self.__html_parser.m_weatherParams):        
                    thisMeasure.wind_speed = self.__html_parser.m_weatherParams['Velocidad viento']
                if ('Dirección viento' in self.__html_parser.m_weatherParams):    
                    thisMeasure.wind_dir = self.__html_parser.m_weatherParams['Dirección viento']
                if ('Temperatura' in self.__html_parser.m_weatherParams):    
                    thisMeasure.temp = self.__html_parser.m_weatherParams['Temperatura']
                if ('Humedad relativa' in self.__html_parser.m_weatherParams):    
                    thisMeasure.hum = self.__html_parser.m_weatherParams['Humedad relativa']
                if ('Presión' in self.__html_parser.m_weatherParams):    
                    thisMeasure.pressure = self.__html_parser.m_weatherParams['Presión']
                if ('Radiación solar' in self.__html_parser.m_weatherParams):    
                    thisMeasure.solar_rad = self.__html_parser.m_weatherParams['Radiación solar']
                if ('Precipitación' in self.__html_parser.m_weatherParams):    
                    thisMeasure.precip = self.__html_parser.m_weatherParams['Precipitación']
                
                # update probe's latest measure reference
                thisProbe.last_measure = thisMeasure

            else:
                print "Error parsing " + thisProbe.name + "\n"
                print "    Station name doesn't match parsed info: " + \
                    self.__html_parser.m_stationName.decode("utf-8") + "\n"


class TresCantosDotEsLiveProbeParser(ProbeParser):
    """
        Parser to retrieve probe data from trescantos.es
        
        There is just 1 probe in a single URL
    """
    
    def __init__(self):
        ProbeParser.__init__(self)
        # the HTML parser info
        self.__html_parser = TresCantosDotEsHTMLParser()
        
        # fill up probe list. Note there is just 1 probe
        #
        self.probe_list.append(
            Probe(u'Tres Cantos', TRESCANTOS_ES_PROBE_TRESCANTOS_URL,
               TRESCANTOS_ES_PROBE_TRESCANTOS_LAT, TRESCANTOS_ES_PROBE_TRESCANTOS_LON))
    
    def update(self):
        print "parsing trescantos.es..."
        # ensure the aprser is clean to start the parsing process
        self.__html_parser.reset()

        req = urllib2.Request(TRESCANTOS_ES_PROBE_TRESCANTOS_URL, data=None, headers=HTTP_HEADERS)
        htmlFile = urllib2.urlopen(req)
    
        # what character encoding set is this file????
        charset = htmlFile.headers.getparam('charset')

        for line in htmlFile.readlines():
            # 
            line = line.strip().decode(charset).encode("utf-8")
            
            try:
                self.__html_parser.feed(line)
            except HTMLParseError, ex:
                print "Exception %s" % (ex.msg)

        htmlFile.close()

        thisMeasure = ProbeMeasure()
        thisMeasure.sample_time = self.__html_parser.m_sampleTime

        if ('NO' in self.__html_parser.m_pollutants):
            thisMeasure.no = self.__html_parser.m_pollutants['NO']
        if ('NO2' in self.__html_parser.m_pollutants):
            thisMeasure.no2 = self.__html_parser.m_pollutants['NO2']
        if ('SO2' in self.__html_parser.m_pollutants):
            thisMeasure.so2 = self.__html_parser.m_pollutants['SO2']
        #TODO
        #if ('NOX' in self.__html_parser.m_pollutants):
        #    thisMeasure.nox = self.__html_parser.m_pollutants['NOX']
        
        if ('Direccion Viento' in self.__html_parser.m_weatherParams):    
            thisMeasure.wind_dir = self.__html_parser.m_weatherParams['Direccion Viento']
        if ('Temperatura' in self.__html_parser.m_weatherParams):    
            thisMeasure.temp = self.__html_parser.m_weatherParams['Temperatura']
        if ('Humedad Relativa' in self.__html_parser.m_weatherParams):    
            thisMeasure.hum = self.__html_parser.m_weatherParams['Humedad Relativa']
        if ('Radiacion Solar' in self.__html_parser.m_weatherParams):    
            thisMeasure.solar_rad = self.__html_parser.m_weatherParams['Radiacion Solar']
        
        self.probe_list[0].last_measure = thisMeasure
 
 
class MunimadridDotEsLiveProbeParser(ProbeParser):
    """
        Parser to retrieve probe data from munimadrid.es
        
        One single URL updates all probes data feed in munimadrid.es.
    """
    
    def __init__(self):
        ProbeParser.__init__(self)
        # the HTML parser info
        self.__html_parser = MunimadridDotEsHTMLParser()
        
        # fill up the probe list. 
        # Note that all probes are updated from the same URL
        #
        self.probe_list.append(
            Probe(u'Madrid - Plaza España', MUNIMADRID_DOT_ES_PROBE_URL,
                MUNIMADRID_DOT_ES_PZAESPANA_LAT, MUNIMADRID_DOT_ES_PZAESPANA_LON))
        self.probe_list.append(
            Probe(u'Madrid - Escuelas Aguirre', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_ESCUELASAGUIRRE_LAT, MUNIMADRID_DOT_ES_ESCUELASAGUIRRE_LON))
        self.probe_list.append(
            Probe(u'Madrid - Avda. Ramon y Cajal', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_RAMONYCAJAL_LAT, MUNIMADRID_DOT_ES_RAMONYCAJAL_LON))
        self.probe_list.append(
            Probe(u'Madrid - Arturo Soria', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_ARTUROSORIA_LAT, MUNIMADRID_DOT_ES_ARTUROSORIA_LON))
        self.probe_list.append(
            Probe(u'Madrid - Villaverde', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_VILLAVERDE_LAT, MUNIMADRID_DOT_ES_VILLAVERDE_LON))
        self.probe_list.append(
            Probe(u'Madrid - Farolillo', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_FAROLILLO_LAT, MUNIMADRID_DOT_ES_FAROLILLO_LON))
        self.probe_list.append(
            Probe(u'Madrid - Casa de Campo', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_CASADECAMPO_LAT, MUNIMADRID_DOT_ES_CASADECAMPO_LON))
        self.probe_list.append(
            Probe(u'Madrid - Barajas pueblo', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_BARAJASPUEBLO_LAT, MUNIMADRID_DOT_ES_BARAJASPUEBLO_LON))
        self.probe_list.append(
            Probe(u'Madrid - Plaza del Carmen', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_PZACARMEN_LAT, MUNIMADRID_DOT_ES_PZACARMEN_LON))
        self.probe_list.append(
            Probe(u'Madrid - Moratalaz', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_MORATALAZ_LAT, MUNIMADRID_DOT_ES_MORATALAZ_LON))
        self.probe_list.append(
            Probe(u'Madrid - Cuatro caminos', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_CUATROCAMINOS_LAT, MUNIMADRID_DOT_ES_CUATROCAMINOS_LON))
        self.probe_list.append(
            Probe(u'Madrid - Barrio del pilar', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_PILAR_LAT, MUNIMADRID_DOT_ES_PILAR_LON))
        self.probe_list.append(
            Probe(u'Madrid - Puente de Vallecas', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_VALLECAS_LAT, MUNIMADRID_DOT_ES_VALLECAS_LON))
        self.probe_list.append(
            Probe(u'Madrid - Mendez Alvaro', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_MENDEZALVARO_LAT, MUNIMADRID_DOT_ES_MENDEZALVARO_LON))
        self.probe_list.append(
            Probe(u'Madrid - Castellana', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_CASTELLANA_LAT, MUNIMADRID_DOT_ES_CASTELLANA_LON))
        self.probe_list.append(
            Probe(u'Madrid - Retiro', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_RETIRO_LAT, MUNIMADRID_DOT_ES_RETIRO_LON))
        self.probe_list.append(
            Probe(u'Madrid - Plaza de Castilla', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_PZACASTILLA_LAT, MUNIMADRID_DOT_ES_PZACASTILLA_LON))
        self.probe_list.append(
            Probe(u'Madrid - Ensanche de Vallecas', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_ENSANCHEVALLECAS_LAT, MUNIMADRID_DOT_ES_ENSANCHEVALLECAS_LON))
        self.probe_list.append(
            Probe(u'Madrid - Urbanizacion embajada', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_URBEMBAJADA_LAT, MUNIMADRID_DOT_ES_URBEMBAJADA_LON))
        self.probe_list.append(
            Probe(u'Madrid - Fernandez Ladreda', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_FDEZLADREDA_LAT, MUNIMADRID_DOT_ES_FDEZLADREDA_LON))
        self.probe_list.append(
            Probe(u'Madrid - Sanchinarro', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_SANCHINARRO_LAT, MUNIMADRID_DOT_ES_SANCHINARRO_LON))
        self.probe_list.append(
            Probe(u'Madrid - El Pardo', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_PARDO_LAT, MUNIMADRID_DOT_ES_PARDO_LON))
        self.probe_list.append(
            Probe(u'Madrid - Juan Carlos I', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_JUANCARLOSI_LAT, MUNIMADRID_DOT_ES_JUANCARLOSI_LON))
        self.probe_list.append(
            Probe(u'Madrid - Tres Olivos', MUNIMADRID_DOT_ES_PROBE_URL,
                 MUNIMADRID_DOT_ES_TRESOLIVOS_LAT, MUNIMADRID_DOT_ES_TRESOLIVOS_LON))
    
    def update(self):
        print "parsing munimadrid.es..."
        # ensure the aprser is clean to start the parsing process
        self.__html_parser.reset()

        req = urllib2.Request(MUNIMADRID_DOT_ES_PROBE_URL, data=None, headers=HTTP_HEADERS)
        htmlFile = urllib2.urlopen(req)
    
        # what character encoding set is this file????
        charset = htmlFile.headers.getparam('charset')

        for line in htmlFile.readlines():
            # munimadrid is UTF-8, but still we should be doing things right
            line = line.strip().decode(charset).encode("utf-8")
            
            try:
                self.__html_parser.feed(line)
            except HTMLParseError, ex:
                print "Exception %s" % (ex.msg)

        htmlFile.close()
                
        for probeEntry in self.__html_parser.m_probePollutantsList:
            # look for the right probe to store the list of pollutants into it
            for probe in self.probe_list:
                if (probe.name[9:].upper() == probeEntry['Estaci\xc3\xb3n'].upper().decode("utf-8")):                    
                    thisMeasure = ProbeMeasure()
                    thisMeasure.sample_time = self.__html_parser.m_sampleTime
                    
                    if ('PM10' in probeEntry):
                        thisMeasure.pm10 = probeEntry['PM10']
                    if ('PM2.5' in probeEntry):
                        thisMeasure.pm25 = probeEntry['PM2.5']
                    if ('SO2' in probeEntry):
                        thisMeasure.so2 = probeEntry['SO2']                        
                    if ('CO' in probeEntry):
                        thisMeasure.co = probeEntry['CO']
                    if ('O3' in probeEntry):
                        thisMeasure.o3 = probeEntry['O3']
                    if ('NO2' in probeEntry):
                        thisMeasure.no2 = probeEntry['NO2']
                    if ('BEN' in probeEntry):
                        thisMeasure.ben = probeEntry['BEN']
                    if ('TOL' in probeEntry):
                        thisMeasure.tol = probeEntry['TOL']
                
                    probe.last_measure = thisMeasure
                    
                    # Found what we were looking for. Exit this loop
                    break
            else:               
                if (probeEntry['Estaci\xc3\xb3n'].upper().decode("utf-8") != 'MEDIA  RED'):
                    # There is no probe that matches this name. 
                    # it always happens with "MEDIA  RED" (network average)
                    print 'Error: Can\'t match probe name: ' + probeEntry['Estaci\xc3\xb3n'].upper()


class JCCMDotEsLiveProbeParser(ProbeParser):
    """
        Parser to retrieve probe data from jccm.es
        
        Each probe has a specific data URL which will be used
        to download the HTML content and parse the live probe feed
    """
    
    def __init__(self):
        ProbeParser.__init__(self)
        # the HTML parser info
        self.__html_parser = JCCMDotEsHTMLParser()
        
        # fill up the probe list. 
        #
        self.probe_list.append(
            Probe(u'Albacete', JCCM_ES_PROBE_ALBACETE_URL,
                JCCM_ES_PROBE_ALBACETE_LAT, JCCM_ES_PROBE_ALBACETE_LON))
        self.probe_list.append(
            Probe(u'Azuqueca', JCCM_ES_PROBE_AZUQUECA_URL,
                JCCM_ES_PROBE_AZUQUECA_LAT, JCCM_ES_PROBE_AZUQUECA_LON))
        self.probe_list.append(
            Probe(u'Guadalajara', JCCM_ES_PROBE_GUADALAJARA_URL,
                JCCM_ES_PROBE_GUADALAJARA_LAT, JCCM_ES_PROBE_GUADALAJARA_LON))
        self.probe_list.append(
            Probe(u'Toledo', JCCM_ES_PROBE_TOLEDO_URL,
                JCCM_ES_PROBE_TOLEDO_LAT, JCCM_ES_PROBE_TOLEDO_LON))
        self.probe_list.append(
            Probe(u'Ciudad Real', JCCM_ES_PROBE_CIUDADREAL_URL,
                JCCM_ES_PROBE_CIUDADREAL_LAT, JCCM_ES_PROBE_CIUDADREAL_LON))
        self.probe_list.append(
            Probe(u'Cuenca', JCCM_ES_PROBE_CUENCA_URL,
                JCCM_ES_PROBE_CUENCA_LAT, JCCM_ES_PROBE_CUENCA_LON))
        self.probe_list.append(
            Probe(u'Illescas', JCCM_ES_PROBE_ILLESCAS_URL,
                JCCM_ES_PROBE_ILLESCAS_LAT, JCCM_ES_PROBE_ILLESCAS_LON))
        self.probe_list.append(
            Probe(u'Talavera', JCCM_ES_PROBE_TALAVERA_URL,
                JCCM_ES_PROBE_TALAVERA_LAT, JCCM_ES_PROBE_TALAVERA_LON))
        self.probe_list.append(
            Probe(u'Puertollano - Calle Ancha', JCCM_ES_PROBE_PUERTOLLANO_CALLEANCHA_URL,
                JCCM_ES_PROBE_PUERTOLLANO_CALLEANCHA_LAT, JCCM_ES_PROBE_PUERTOLLANO_CALLEANCHA_LON))
        self.probe_list.append(
            Probe(u'Puertollano - Instituto', JCCM_ES_PROBE_PUERTOLLANO_INSTITUTO_URL,
                JCCM_ES_PROBE_PUERTOLLANO_INSTITUTO_LAT, JCCM_ES_PROBE_PUERTOLLANO_INSTITUTO_LON))
        self.probe_list.append(
            Probe(u'Puertollano - Campo de fútbol', JCCM_ES_PROBE_PUERTOLLANO_CAMPOFUTBOL_URL,
                JCCM_ES_PROBE_PUERTOLLANO_CAMPOFUTBOL_LAT, JCCM_ES_PROBE_PUERTOLLANO_CAMPOFUTBOL_LON))
        self.probe_list.append(
            Probe(u'Puertollano - Barriada 630', JCCM_ES_PROBE_PUERTOLLANO_B630_URL,
                JCCM_ES_PROBE_PUERTOLLANO_B630_LAT, JCCM_ES_PROBE_PUERTOLLANO_B630_LON))

    def update(self):
        for thisProbe in self.probe_list:
            print "parsing jccm.es - " + thisProbe.name + "..."
            # ensure the parser is clean to start the parsing process
            self.__html_parser.reset()

            req = urllib2.Request(thisProbe.dataURL, data=None, headers=HTTP_HEADERS)
            htmlFile = urllib2.urlopen(req)
        
            # what character encoding set is this file????
            charset = htmlFile.headers.getparam('charset')

            for line in htmlFile.readlines():
                # jccm.es is ISO-8859-1
                line = line.strip().decode(charset).encode("utf-8")

                try:
                    self.__html_parser.feed(line)
                except HTMLParseError, ex:
                    print "Exception %s" % (ex.msg)

            htmlFile.close()
            
            thisMeasure = ProbeMeasure()
            thisMeasure.sample_time = self.__html_parser.m_sampleTime            
                
            if ('CO' in self.__html_parser.m_pollutants):
                thisMeasure.co = self.__html_parser.m_pollutants['CO']
            if ('NO' in self.__html_parser.m_pollutants):
                thisMeasure.no = self.__html_parser.m_pollutants['NO']
            if ('NO2' in self.__html_parser.m_pollutants):
                thisMeasure.no2 = self.__html_parser.m_pollutants['NO2']
            if ('SO2' in self.__html_parser.m_pollutants):
                thisMeasure.so2 = self.__html_parser.m_pollutants['SO2']
            if ('PM2,5' in self.__html_parser.m_pollutants):
                thisMeasure.pm25 = self.__html_parser.m_pollutants['PM2,5']
            if ('PM10' in self.__html_parser.m_pollutants):
                thisMeasure.pm10 = self.__html_parser.m_pollutants['PM10']
            if ('O3' in self.__html_parser.m_pollutants):
                thisMeasure.o3 = self.__html_parser.m_pollutants['O3']
            if ('SH2' in self.__html_parser.m_pollutants):
                thisMeasure.sh2 = self.__html_parser.m_pollutants['SH2']
            if ('TOL' in self.__html_parser.m_pollutants):
                thisMeasure.tol = self.__html_parser.m_pollutants['TOL']
            if ('BEN' in self.__html_parser.m_pollutants):
                thisMeasure.ben = self.__html_parser.m_pollutants['BEN']
            if ('XIL' in self.__html_parser.m_pollutants):
                thisMeasure.xyl = self.__html_parser.m_pollutants['XIL']
            
            # update probe's latest measure
            thisProbe.last_measure = thisMeasure



class AirecantabriaLiveProbeParser(ProbeParser):
    """
        Parser to retrieve probe data from airecantabria.com
        
        Each probe has a specific data URL which will be used
        to download the HTML content and parse the live probe feed
    """
    
    def __init__(self):
        ProbeParser.__init__(self)
        # the HTML parser info
        self.__html_parser = AirecantabriaHTMLParser()
        
        # fill up the probe list. 
        #
        self.probe_list.append(
            Probe(u'Santander - Centro', AIRECANTABRIA_COM_PROBE_SANTANDER_CENTRO_URL,
                AIRECANTABRIA_COM_PROBE_SANTANDER_CENTRO_LAT, AIRECANTABRIA_COM_PROBE_SANTANDER_CENTRO_LON))
        self.probe_list.append(
            Probe(u'Santander - Tetuán', AIRECANTABRIA_COM_PROBE_SANTANDER_TETUAN_URL,
                AIRECANTABRIA_COM_PROBE_SANTANDER_TETUAN_LAT, AIRECANTABRIA_COM_PROBE_SANTANDER_TETUAN_LON))
        self.probe_list.append(
            Probe(u'Cros-Camargo', AIRECANTABRIA_COM_PROBE_CAMARGO_URL,
                AIRECANTABRIA_COM_PROBE_CAMARGO_LAT, AIRECANTABRIA_COM_PROBE_CAMARGO_LON))
        self.probe_list.append(
            Probe(u'Guarnizo', AIRECANTABRIA_COM_PROBE_GUARNIZO_URL,
                AIRECANTABRIA_COM_PROBE_GUARNIZO_LAT, AIRECANTABRIA_COM_PROBE_GUARNIZO_LON))
        self.probe_list.append(
            Probe(u'Torrelavega - Escuela de Minas', AIRECANTABRIA_COM_PROBE_TORRELAVEGA_MINAS_URL,
                AIRECANTABRIA_COM_PROBE_TORRELAVEGA_MINAS_LAT, AIRECANTABRIA_COM_PROBE_TORRELAVEGA_MINAS_LON))
        self.probe_list.append(
            Probe(u'Torrelavega - Parque Zapatón', AIRECANTABRIA_COM_PROBE_TORRELAVEGA_ZAPATON_URL,
                AIRECANTABRIA_COM_PROBE_TORRELAVEGA_ZAPATON_LAT, AIRECANTABRIA_COM_PROBE_TORRELAVEGA_ZAPATON_LON))
        self.probe_list.append(
            Probe(u'Torrelavega - Barreda', AIRECANTABRIA_COM_PROBE_TORRELAVEGA_BARREDA_URL,
                AIRECANTABRIA_COM_PROBE_TORRELAVEGA_BARREDA_LAT, AIRECANTABRIA_COM_PROBE_TORRELAVEGA_BARREDA_LON))
#        self.probe_list.append(
#            Probe(u'Torrelavega - C.I.M.A.', AIRECANTABRIA_COM_PROBE_TORRELAVEGA_CIMA_URL,
#                AIRECANTABRIA_COM_PROBE_TORRELAVEGA_CIMA_LAT, AIRECANTABRIA_COM_PROBE_TORRELAVEGA_CIMA_LON))
        self.probe_list.append(
            Probe(u'Los Corrales de Buelna', AIRECANTABRIA_COM_PROBE_BUELNA_URL,
                AIRECANTABRIA_COM_PROBE_BUELNA_LAT, AIRECANTABRIA_COM_PROBE_BUELNA_LON))
        self.probe_list.append(
            Probe(u'Reinosa', AIRECANTABRIA_COM_PROBE_REINOSA_URL,
                AIRECANTABRIA_COM_PROBE_REINOSA_LAT, AIRECANTABRIA_COM_PROBE_REINOSA_LON))
        self.probe_list.append(
            Probe(u'Los Tojos', AIRECANTABRIA_COM_PROBE_TOJOS_URL,
                AIRECANTABRIA_COM_PROBE_TOJOS_LAT, AIRECANTABRIA_COM_PROBE_TOJOS_LON))
        self.probe_list.append(
            Probe(u'Castro Urdiales', AIRECANTABRIA_COM_PROBE_CASTRO_URL,
                AIRECANTABRIA_COM_PROBE_CASTRO_LAT, AIRECANTABRIA_COM_PROBE_CASTRO_LON))
    
    def update(self):
        for thisProbe in self.probe_list:
            print "parsing airecantabria.com - " + thisProbe.name + "..."
            # ensure the aprser is clean to start the parsing process
            self.__html_parser.reset()

            req = urllib2.Request(thisProbe.dataURL, data=None, headers=HTTP_HEADERS)
            htmlFile = urllib2.urlopen(req)
        
            # charset detection fails in airecantabria.com
            #charset = htmlFile.headers.getparam('charset')

            lineCount = 0
            for line in htmlFile.readlines():
                # airecantabria.com is UTF-8                
                lineCount = lineCount + 1

                # parsing these URLs go bananas before this line
                if (lineCount > 199):
                    line = line.strip()
                    try:
                        self.__html_parser.feed(line)
                    except HTMLParseError, ex:
                        print "Exception %s" % (ex.msg)

            htmlFile.close()
            
            thisMeasure = ProbeMeasure()
            thisMeasure.sample_time = self.__html_parser.m_sampleTime

            if ('CO' in self.__html_parser.m_pollutants):
                thisMeasure.co = self.__html_parser.m_pollutants['CO']
            if ('NO' in self.__html_parser.m_pollutants):
                thisMeasure.no = self.__html_parser.m_pollutants['NO']
            if ('NO2' in self.__html_parser.m_pollutants):
                thisMeasure.no2 = self.__html_parser.m_pollutants['NO2']
            if ('SO2' in self.__html_parser.m_pollutants):
                thisMeasure.so2 = self.__html_parser.m_pollutants['SO2']
            if ('PM10' in self.__html_parser.m_pollutants):
                thisMeasure.pm10 = self.__html_parser.m_pollutants['PM10']
            if ('O3' in self.__html_parser.m_pollutants):
                thisMeasure.o3 = self.__html_parser.m_pollutants['O3']
            if ('SH2' in self.__html_parser.m_pollutants):
                thisMeasure.sh2 = self.__html_parser.m_pollutants['SH2']
            if ('TOL' in self.__html_parser.m_pollutants):
                thisMeasure.tol = self.__html_parser.m_pollutants['TOL']
            if ('BEN' in self.__html_parser.m_pollutants):
                thisMeasure.ben = self.__html_parser.m_pollutants['BEN']
            if ('XIL' in self.__html_parser.m_pollutants):
                thisMeasure.xyl = self.__html_parser.m_pollutants['XIL']
            
            if (len(self.__html_parser.m_weatherParams) > 0):
                if ('VV' in self.__html_parser.m_weatherParams):        
                    thisMeasure.wind_speed = self.__html_parser.m_weatherParams['VV']
                if ('DD' in self.__html_parser.m_weatherParams):    
                    thisMeasure.wind_dir = self.__html_parser.m_weatherParams['DD']
                if ('TMP' in self.__html_parser.m_weatherParams):    
                    thisMeasure.temp = self.__html_parser.m_weatherParams['TMP']
                if ('HR' in self.__html_parser.m_weatherParams):    
                    thisMeasure.hum = self.__html_parser.m_weatherParams['HR']
                if ('PRB' in self.__html_parser.m_weatherParams):    
                    thisMeasure.pressure = self.__html_parser.m_weatherParams['PRB']
                if ('RS' in self.__html_parser.m_weatherParams):    
                    thisMeasure.solar_rad = self.__html_parser.m_weatherParams['RS']
                if ('LL' in self.__html_parser.m_weatherParams):    
                    thisMeasure.precip = self.__html_parser.m_weatherParams['LL']
            
            # update probe's latest measure reference
            thisProbe.last_measure = thisMeasure



class AragonaireDotEsLiveProbeParser(ProbeParser):
    """
        Parser to retrieve probe data from aragonaire.es
        
        Each probe has a specific data URL which will be used
        to download the HTML content and parse the live probe feed
    """
    
    def __init__(self):
        ProbeParser.__init__(self)
        # the HTML parser info
        self.__html_parser = AragonaireHTMLParser()
        
        # fill up the probe list. 
        #
        self.probe_list.append(
            Probe(u'Alagón', ARAGONAIRE_ES_PROBE_ALAGON_URL, 
                ARAGONAIRE_ES_PROBE_ALAGON_LAT, ARAGONAIRE_ES_PROBE_ALAGON_LON))
        self.probe_list.append(
            Probe(u'Bujaraloz', ARAGONAIRE_ES_PROBE_BUJARALOZ_URL, 
                ARAGONAIRE_ES_PROBE_BUJARALOZ_LAT, ARAGONAIRE_ES_PROBE_BUJARALOZ_LON))
        self.probe_list.append(
            Probe(u'Huesca', ARAGONAIRE_ES_PROBE_HUESCA_URL, 
                ARAGONAIRE_ES_PROBE_HUESCA_LAT, ARAGONAIRE_ES_PROBE_HUESCA_LON))
        self.probe_list.append(
            Probe(u'Monzón', ARAGONAIRE_ES_PROBE_MONZON_URL, 
                ARAGONAIRE_ES_PROBE_MONZON_LAT, ARAGONAIRE_ES_PROBE_MONZON_LON))
        self.probe_list.append(
            Probe(u'Teruel', ARAGONAIRE_ES_PROBE_TERUEL_URL, 
                ARAGONAIRE_ES_PROBE_TERUEL_LAT, ARAGONAIRE_ES_PROBE_TERUEL_LON))
        self.probe_list.append(
            Probe(u'Torrelisa', ARAGONAIRE_ES_PROBE_TORRELISA_URL, 
                ARAGONAIRE_ES_PROBE_TORRELISA_LAT, ARAGONAIRE_ES_PROBE_TORRELISA_LON))

    def update(self):
        for thisProbe in self.probe_list:
            print "parsing aragonaire.es - " + thisProbe.name + "..."
            # ensure the aprser is clean to start the parsing process
            self.__html_parser.reset()

            req = urllib2.Request(thisProbe.dataURL, data=None, headers=HTTP_HEADERS)
            htmlFile = urllib2.urlopen(req)
        
            # charset detection fails in airecantabria.com
            #charset = htmlFile.headers.getparam('charset')

            for line in htmlFile.readlines():
                # aragonaire is UTF-8  
                line = line.strip()

                try:
                    self.__html_parser.feed(line)
                except HTMLParseError, ex:
                    print "Exception %s" % (ex.msg)

            htmlFile.close()
            
            thisMeasure = ProbeMeasure()
            thisMeasure.sample_time = self.__html_parser.m_sampleTime

            if ('CO' in self.__html_parser.m_pollutants):
                thisMeasure.co = self.__html_parser.m_pollutants['CO']
            if ('NO2' in self.__html_parser.m_pollutants):
                thisMeasure.no2 = self.__html_parser.m_pollutants['NO2']
            if ('SO2' in self.__html_parser.m_pollutants):
                thisMeasure.so2 = self.__html_parser.m_pollutants['SO2']
            if ('O3' in self.__html_parser.m_pollutants):
                thisMeasure.o3 = self.__html_parser.m_pollutants['O3']
            
            # update probe's latest measure reference
            thisProbe.last_measure = thisMeasure



class AsturiasDotEsLiveProbeParser(ProbeParser):
    """
        Parser to retrieve probe data from asturias.es
        
        This is a temporary solution to be able to show the probes coordinates
        on the map. It does no parsing whatsoever
    """
    
    def __init__(self):
        ProbeParser.__init__(self)
        
        # fill up the probe list. 
        #
        self.probe_list.append(
            Probe(u'Avilés - Llano Ponte', '', 
                ASTURIAS_ES_PROBE_AVILES_LLANOPONTE_LAT, ASTURIAS_ES_PROBE_AVILES_LLANOPONTE_LON))
        self.probe_list.append(
            Probe(u'Avilés - Plaza Guitarra', '', 
                 ASTURIAS_ES_PROBE_AVILES_PZAGUITARRA_LAT, ASTURIAS_ES_PROBE_AVILES_PZAGUITARRA_LON))
        self.probe_list.append(
            Probe(u'Avilés - Matadero', '', 
                 ASTURIAS_ES_PROBE_AVILES_MATADERO_LAT, ASTURIAS_ES_PROBE_AVILES_MATADERO_LON))
        self.probe_list.append(
            Probe(u'Avilés - Llaranes', '', 
                 ASTURIAS_ES_PROBE_AVILES_LLARANES_LAT, ASTURIAS_ES_PROBE_AVILES_LLARANES_LON))
        self.probe_list.append(
            Probe(u'Gijón - Plaza Castilla', '', 
                 ASTURIAS_ES_PROBE_GIJON_CASTILLA_LAT, ASTURIAS_ES_PROBE_GIJON_CASTILLA_LON))
        self.probe_list.append(
            Probe(u'Gijón - Avda. Argentina', '', 
                 ASTURIAS_ES_PROBE_GIJON_ARGENTINA_LAT, ASTURIAS_ES_PROBE_GIJON_ARGENTINA_LON))
        self.probe_list.append(
            Probe(u'Gijón - Avda. Constitución', '', 
                 ASTURIAS_ES_PROBE_GIJON_CONSTITUTION_LAT, ASTURIAS_ES_PROBE_GIJON_CONSTITUCION_LON))
        self.probe_list.append(
            Probe(u'Gijón - Montevil', '', 
                 ASTURIAS_ES_PROBE_GIJON_MONTEVIL_LAT, ASTURIAS_ES_PROBE_GIJON_MONTEVIL_LON))
        self.probe_list.append(
            Probe(u'Gijón - H. Felgueroso', '', 
                 ASTURIAS_ES_PROBE_GIJON_HFELGUEROSO_LAT, ASTURIAS_ES_PROBE_GIJON_HFELGUEROSO_LON))
        self.probe_list.append(
            Probe(u'Langreo - La Felguera', '', 
                 ASTURIAS_ES_PROBE_LANGREO_FELGUERA_LAT, ASTURIAS_ES_PROBE_LANGREO_FELGUERA_LON))
        self.probe_list.append(
            Probe(u'Langreo - Meriñán', '', 
                 ASTURIAS_ES_PROBE_LANGREO_MERINAN_LAT, ASTURIAS_ES_PROBE_LANGREO_MERINAN_LON))
        self.probe_list.append(
            Probe(u'Langreo - Sama', '', 
                 ASTURIAS_ES_PROBE_LANGREO_SAMA_LAT, ASTURIAS_ES_PROBE_LANGREO_SAMA_LON))
        self.probe_list.append(
            Probe(u'San Martín - El Florán', '', 
                 ASTURIAS_ES_PROBE_SMARTIN_FLORAN_LAT, ASTURIAS_ES_PROBE_SMARTIN_FLORAN_LON))
        self.probe_list.append(
            Probe(u'Mieres', '', 
                 ASTURIAS_ES_PROBE_MIERES_LAT, ASTURIAS_ES_PROBE_MIERES_LON))
        self.probe_list.append(
            Probe(u'Oviedo - Trubia', '', 
                 ASTURIAS_ES_PROBE_OVIEDO_TRUBIA_LAT, ASTURIAS_ES_PROBE_OVIEDO_TRUBIA_LON))
        self.probe_list.append(
            Probe(u'Oviedo - Purificación Tomás', '', 
                 ASTURIAS_ES_PROBE_OVIEDO_PTOMAS_LAT, ASTURIAS_ES_PROBE_OVIEDO_PTOMAS_LON))
        self.probe_list.append(
            Probe(u'Oviedo - Plaza de Toros', '', 
                 ASTURIAS_ES_PROBE_OVIEDO_PTOROS_LAT, ASTURIAS_ES_PROBE_OVIEDO_PTOROS_LON))
        self.probe_list.append(
            Probe(u'Oviedo - Palacio Deportes', '', 
                 ASTURIAS_ES_PROBE_OVIEDO_PDEPORTES_LAT, ASTURIAS_ES_PROBE_OVIEDO_PDEPORTES_LON))
        self.probe_list.append(
            Probe(u'Siero - Lugones', '', 
                 ASTURIAS_ES_PROBE_LUGONES_LAT, ASTURIAS_ES_PROBE_LUGONES_LON))
        self.probe_list.append(
            Probe(u'Cangas del Narcea', '', 
                 ASTURIAS_ES_PROBE_CANGASNARCEA_LAT, ASTURIAS_ES_PROBE_CANGASNARCEA_LON))
        
    def update(self):
        #TODO it does nothing for now
        pass

