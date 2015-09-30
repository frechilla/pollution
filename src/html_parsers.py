import re
from HTMLParser import HTMLParser
from HTMLParser import HTMLParseError
from datetime import datetime

import pytz
from pytz import timezone

# Enum for all states in case state machines are needed
# 
class State(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError
    
# states for the parsing state machine
#
STATES = State([
    "IDLE", 
    "STATION_NAME__WAITING_STRONG",
    "STATION_NAME__READY",
    "SAMPLE_TIME__WAITING_STRONG",
    "SAMPLE_TIME__READY",
    "DATA_PAIRS__TITLE",
    "DATA_PAIRS__POLLUTANTS",
    "DATA_PAIRS__WEATHER"])

class  MadridDotOrgHTMLParser(HTMLParser):
    """
    HTML parser for probes shown in madrid.org
    """
    
    def __init__(self):
        # call the parent constructor first
        HTMLParser.__init__(self)
        self.__initiliaseParser()
        
        # regex to parse time
        self.__datetimeRegex = re.compile('([0-9]+):([0-9]+).*')
    
    def __initiliaseParser(self):
        # current state of the parser machine state
        self.__state = STATES.IDLE
        
        # private data members to parse the data pairs (key + datum)
        self.__tr_pollutant = False
        self.__tr_weatherParam = False
        self.__tag_small = False
        self.__currentPollutantKey = ""
        self.__currentWeatherParamKey = ""
        self.__sampleDaytime = ""
        
        # member variables
        self.m_stationName = ""
        self.m_sampleTime = None
        try:
            self.m_pollutants.clear()
        except AttributeError:
            self.m_pollutants = {} # empty dict
        try:
            self.m_weatherParams.clear()
        except AttributeError:
            self.m_weatherParams = {} # empty dict
        
    def reset(self):
        # reset all object's attributes
        self.__initiliaseParser()
        # call the parent reset too
        HTMLParser.reset(self)
    
    def handle_starttag(self, tag, attrs):
        if (tag == 'td'):
            # attrs is a list of tuple pairs, a dictionary is more useful
            dattrs = dict(attrs)
            
            # station name
            if (('colspan' in dattrs) and (dattrs['colspan'] == '2') and
               ('class' in dattrs) and (dattrs['class'] == 'txt11neg')):
                self.__state = STATES.STATION_NAME__WAITING_STRONG
            # Sample time
            elif (('colspan' in dattrs) and (dattrs['colspan'] == '2') and
               ('align' in dattrs) and (dattrs['align'] == 'center') and
               ('id' in dattrs) and (dattrs['id'] == 'fondoGrisMedio') and
               ('class' in dattrs) and (dattrs['class'] == 'txt11bla')):
                self.__state = STATES.SAMPLE_TIME__WAITING_STRONG
            # pollutants
            elif (('colspan' in dattrs) and (dattrs['colspan'] == '2') and
               ('id' in dattrs) and (dattrs['id'] == 'fondoGris') and
               ('class' in dattrs) and (dattrs['class'] == 'txt11azu')):
                self.__state = STATES.DATA_PAIRS__TITLE
        
        elif (tag == 'tr'):
            # specific pollutant
            if (self.__state == STATES.DATA_PAIRS__POLLUTANTS):
                self.__tr_pollutant = True
            # specific weather param
            elif (self.__state == STATES.DATA_PAIRS__WEATHER):
                self.__tr_weatherParam = True
        
        elif (tag == 'strong'):
            # station name
            if (self.__state == STATES.STATION_NAME__WAITING_STRONG):
                self.__state = STATES.STATION_NAME__READY
            # Sample time
            if (self.__state == STATES.SAMPLE_TIME__WAITING_STRONG):
                self.__state = STATES.SAMPLE_TIME__READY
        
        elif (tag == 'small'):
            self.__tag_small = True

    def handle_endtag(self, tag):
        if (tag == 'tr'):
            # row for a specific pollutant
            if (self.__tr_pollutant):
                if (self.__currentPollutantKey in self.m_pollutants and
                    self.m_pollutants[self.__currentPollutantKey].startswith('**')):
                    # '***N' is an invalid value. Same as "no data"
                    # reset its value to the empty string
                    #
                    # http://gestiona.madrid.org/azul_internet/html/web/2_4.htm?ESTADO_MENU=2_1_3
                    #   Z- Dato de calibracion de cero.
                    #   C- Dato de calibracion de span.
                    #   M- Dato de mantenimiento.
                    #   F- Fallo de tensión.
                    #   N- Dato invalido por causa desconocida (fuera de rango).
                    #   D- Fallo tecnico del analizador. 
                    del self.m_pollutants[self.__currentPollutantKey]
                    self.m_pollutants[self.__currentPollutantKey] = ""
                    
                self.__tr_pollutant = False
                self.__currentPollutantKey = ""
                
            # row for a specific weather param
            elif (self.__tr_weatherParam):
                if (self.__currentWeatherParamKey in self.m_weatherParams and
                    self.m_weatherParams[self.__currentWeatherParamKey].startswith('**')):
                    # '***N' is an invalid value. Same as "no data"
                    # reset its value to the empty string
                    del self.m_weatherParams[self.__currentWeatherParamKey]
                    self.m_weatherParams[self.__currentWeatherParamKey] = ""
                    
                self.__tr_weatherParam = False
                self.__currentWeatherParamKey = ""
                
        elif (tag == 'table'):
            if ((self.__state == STATES.DATA_PAIRS__POLLUTANTS) or 
                (self.__state == STATES.DATA_PAIRS__WEATHER)):
                self.__state = STATES.IDLE
             
        elif (tag == 'strong'):
            # station name
            if (self.__state == STATES.STATION_NAME__READY):
                self.__state = STATES.IDLE
            # Sample time
            elif (self.__state == STATES.SAMPLE_TIME__READY):
                self.__state = STATES.IDLE
                
                result = self.__datetimeRegex.search(self.__sampleDaytime)
                if (result != None):
                    utc = pytz.utc
                    self.m_sampleTime = \
                        utc.localize(datetime.now().replace(hour=int(result.group(1)), minute=int(result.group(2)), second=0, microsecond=0))
                else:
                    print "Error parsing sample time"
        
        elif (tag == 'small'):
            self.__tag_small = False
        
    def handle_data(self, data):
        data = data.strip()
        if (data <> ''):
            if (self.__state == STATES.STATION_NAME__READY):
                # 13 is the index to remove "Estación de " from the station name
                self.m_stationName = data[13:]
            elif (self.__state == STATES.SAMPLE_TIME__READY):
                # It doesn not have a '+=' because we're using a dirty trick 
                # here to remove the first line of the current date. It normally
                # contains: 'Ultima media horaria a las' and we just want the
                # hh:mm
                self.__sampleDaytime = data
            elif (self.__state == STATES.DATA_PAIRS__TITLE):
                if (data.startswith('Contaminantes')):
                    self.__state = STATES.DATA_PAIRS__POLLUTANTS
                elif (data.startswith('Meteorolog')):
                    self.__state = STATES.DATA_PAIRS__WEATHER
                else:
                    print 'Error parsing type of data: "%s"' % (data)
            elif (self.__state == STATES.DATA_PAIRS__POLLUTANTS):
                if (not self.__tag_small):
                    if (self.__currentPollutantKey == ""):
                        self.__currentPollutantKey = data
                    elif (self.__tr_pollutant):
                        if (self.__currentPollutantKey in self.m_pollutants):
                            tmp = self.m_pollutants[self.__currentPollutantKey]
                            del self.m_pollutants[self.__currentPollutantKey]
                            self.m_pollutants[self.__currentPollutantKey] = tmp + data
                        else:
                            self.m_pollutants[self.__currentPollutantKey] = data
                        
            elif (self.__state == STATES.DATA_PAIRS__WEATHER):
                if (not self.__tag_small):
                    if (self.__currentWeatherParamKey == ""):
                        self.__currentWeatherParamKey = data
                    elif (self.__tr_weatherParam):
                        if (self.__currentWeatherParamKey in self.m_weatherParams):
                            tmp = self.m_weatherParams[self.__currentWeatherParamKey]
                            del self.m_weatherParams[self.__currentWeatherParamKey]
                            self.m_weatherParams[self.__currentWeatherParamKey] = tmp + data
                        else:
                            self.m_weatherParams[self.__currentWeatherParamKey] = data



class  MunimadridDotEsHTMLParser(HTMLParser):
    """
    HTML parser for probes shown in munimadrid.es
    """

    def __init__(self):
        # call the parent constructor first
        HTMLParser.__init__(self)
        self.__initiliaseParser()
        
        # regex to parse time
        self.__datetimeRegex = re.compile('([0-9]+)/([0-9]+)/([0-9]+) ([0-9]+):([0-9]+).*')
        
    def __initiliaseParser(self):
        # private data members to parse the data pairs (key + datum)
        self.__table_data = False
        self.__tr_data_row = False
        self.__td_header = ""
        self.__span_sampletime = False
        self.__span_sampledate = False
        self.__sampleDaytime = ''
        try:
            self.__probePollutants.clear()
        except AttributeError:
            self.__probePollutants = {} # empty dict
        
        # member variables
        self.m_sampleTime = None
        try:
            del self.m_probePollutantsList[:]
        except AttributeError:
            self.m_probePollutantsList = list() # empty list of dicts
        
    def reset(self):
        # reset all object's attributes
        self.__initiliaseParser()
        # call the parent reset too
        HTMLParser.reset(self)
    
    def handle_starttag(self, tag, attrs):
        if (tag == 'table'):
            dattrs = dict(attrs)
            if (('cellpadding' in dattrs and dattrs['cellpadding'] == '0') and
                ('cellspacing' in dattrs and dattrs['cellspacing'] == '0') and
                ('class' in dattrs and dattrs['class'] == 'tabla_1 numeros inf_diario') and
                ('summary' in dattrs and dattrs['summary'].endswith('Red de Vigilancia de la Calidad del Aire del Ayuntamiento de Madrid'))):
                self.__table_data = True
        elif (tag == 'tr'):
            if (self.__table_data and len(attrs) == 0):
                self.__tr_data_row = True
        elif (tag == 'td'):
            dattrs = dict(attrs)
            if ('headers' in dattrs):
                self.__td_header = dattrs['headers']
            else:
                self.__td_header = ''
        elif (tag == 'span'):
            if (self.__table_data):
                dattrs = dict(attrs)
                if ('class' in dattrs and dattrs['class'] == 'tabla_titulo_hora'):
                    self.__span_sampletime = True
                elif ('class' in dattrs and dattrs['class'] == 'tabla_titulo_fecha'):
                    self.__span_sampledate = True

    def handle_endtag(self, tag):
        if (tag == 'table'):
            if (self.__table_data):
                self.__table_data = False
        elif (tag == 'tr'):
            if (self.__tr_data_row):
                self.__tr_data_row = False
                self.m_probePollutantsList.append(self.__probePollutants)
                self.__probePollutants = {}
        elif (tag == 'td'):
            self.__td_header = ""
        elif (tag == 'span'):
            if (self.__span_sampletime):
                self.__span_sampletime = False
            elif (self.__span_sampledate):
                self.__span_sampledate = False
        
    def handle_data(self, data):
        if (self.__tr_data_row and self.__td_header != ""):
            # this is some data we should read
            #
            # '-' means NO DATA available
            #
            data = data.strip()
            if (data != ''):
                if (data == '-'):
                    data = ''
                self.__probePollutants[self.__td_header] = data
        elif (self.__span_sampletime):
            self.__sampleDaytime = self.__sampleDaytime + ' ' + data
            
            result = self.__datetimeRegex.search(self.__sampleDaytime)
            if (result != None):
                madrid = pytz.timezone('Europe/Madrid')
                self.m_sampleTime = madrid.localize(datetime(
                        year = int(result.group(3)),
                        month = int(result.group(2)),
                        day = int(result.group(1)),
                        hour=int(result.group(4)),
                        minute=int(result.group(5)),
                        second=0, 
                        microsecond=0))
            else:
                print "Error parsing sample time '%s'" % (self.__sampleDaytime)
            
        elif (self.__span_sampledate):
            self.__sampleDaytime = data



class TresCantosDotEsHTMLParser(HTMLParser):
    """
    HTML parser for probe in trescantos.es
    """
    pass

    def __init__(self):
        # call the parent constructor first
        HTMLParser.__init__(self)
        self.__initiliaseParser()
        
        # regex to parse time
        self.__datetimeRegex = re.compile('Calidad del Aire - Dia ([0-9]+)/([0-9]+) a la[s]* ([0-9]+):([0-9]+) h.')

    def __initiliaseParser(self):
        # private data members to parse the data pairs (key + datum)
        self.__tr = False
        self.__td = False
        self.__h3 = False
        self.__key = ""
        self.__datum = ""
        self.__data = ""

        self.m_sampleTime = None
        try:
            self.m_pollutants.clear()
        except AttributeError:
            self.m_pollutants = {} # empty dict
        try:
            self.m_weatherParams.clear()
        except AttributeError:
            self.m_weatherParams = {} # empty dict
        
    def reset(self):
        # reset all object's attributes
        self.__initiliaseParser()
        # call the parent reset too
        HTMLParser.reset(self)

    def handle_starttag(self, tag, attrs):
        if (tag == 'tr'):
            self.__tr = True
        elif (tag == 'td'):
            self.__td = True
        elif (tag == 'h3'):
            self.__h3 = True

    def handle_endtag(self, tag):
        if (tag == 'tr'):
             self.__tr = False
             self.__key = self.__datum = ""
        elif (tag == 'td'):
            if (self.__key == ""):
                self.__key = self.__data
            elif (self.__data != ""):
                self.__datum = self.__data
                if (self.__key == 'Direccin Viento'):
                    self.m_weatherParams['Direccion Viento'] = self.__datum
                elif (self.__key == 'NO'):
                    self.m_pollutants['NO'] = self.__datum
                elif (self.__key == 'Temperatura'):
                    self.m_weatherParams['Temperatura'] = self.__datum
                elif (self.__key == 'NO2'):
                    self.m_pollutants['NO2'] = self.__datum
                elif (self.__key == 'HR'):
                    self.m_weatherParams['Humedad Relativa'] = self.__datum
                elif (self.__key == 'NOX'):
                    self.m_pollutants['NOX'] = self.__datum
                elif (self.__key == 'Radiacin Solar'):
                    self.m_weatherParams['Radiacion Solar'] = self.__datum
                elif (self.__key == 'SO2'):
                    self.m_pollutants['SO2'] = self.__datum
                else:
                    self.__key = self.__data
                    self.__datum = ""
                if (self.__datum != ""):
                    self.__key = self.__datum = ""
            self.__data = ""
            self.__td = False
        elif (tag == 'h3'):
            self.__h3 = False

    def handle_data(self, data):
        if (self.__tr):
            self.__data += data.strip()
        elif (self.__h3):
            result = self.__datetimeRegex.search(data.strip())
            if (result != None):
                madrid = pytz.timezone('Europe/Madrid')
                self.m_sampleTime = madrid.localize(datetime(
                        year = datetime.now().year,
                        month = int(result.group(2)),
                        day = int(result.group(1)),
                        hour= int(result.group(3)),
                        minute= int(result.group(4)),
                        second=0, 
                        microsecond=0))
            else:
                print "Error parsing sample time '%s'" % (data.strip())



class  JCCMDotEsHTMLParser(HTMLParser):
    """
    HTML parser for probes shown in jccm.es
    """

    def __init__(self):
        # call the parent constructor first
        HTMLParser.__init__(self)
        self.__initiliaseParser()
        
        # regex to parse time
        self.__datetimeRegex = re.compile('.* ([0-9]+)-([A-Za-z]+)-([0-9]+) ([0-9]+):([0-9]+)')
        
        # regex to parse data pairs (key + datum)
        self.__pollutantNameRegex = re.compile('.*\(([0-9A-Z\.,]+)\).*')
        self.__pollutantDatumRegex = re.compile('^([0-9\.,]+).*')

    def __initiliaseParser(self):
        # private data members to parse the HTML entry 
        self.__tableCount = 0
        self.__td_sampletime = False
        self.__pollutantRow = False
        self.__pollutantName = ''
        self.__pollutantDatum = ''
        
        # member variables
        self.m_sampleTime = None
        try:
            self.m_pollutants.clear()
        except AttributeError:
            self.m_pollutants = {} # empty dict
        
    def reset(self):
        # reset all object's attributes
        self.__initiliaseParser()
        # call the parent reset too
        HTMLParser.reset(self)
    
    def handle_starttag(self, tag, attrs):
        if (tag == 'table'):
            self.__tableCount = self.__tableCount + 1              
        elif (tag == 'td'):
            dattrs = dict(attrs)
            if ((self.__tableCount == 2) and
                ('height' in dattrs and dattrs['height'] == '20')):
                self.__td_sampletime = True
        elif (tag == 'font'):
            dattrs = dict(attrs)
            if ((self.__tableCount == 4) and
                ('color' in dattrs and dattrs['color'] == '#002D59') and
                ('size' in dattrs and dattrs['size'] == '2') and
                ('face' in dattrs and dattrs['face'] == 'Arial, Helvetica, sans-serif')):
                self.__pollutantRow = True

    def handle_endtag(self, tag):
        if (tag == 'table'):
            self.__tableCount = self.__tableCount - 1            
            if (self.__tableCount == 4) and (self.__pollutantName != ''):  
                result = self.__pollutantNameRegex.search(self.__pollutantName)
                if (result != None):
                    self.__pollutantName = result.group(1)
                    
                    result = self.__pollutantDatumRegex.search(self.__pollutantDatum)
                    if (result != None):
                        self.__pollutantDatum = result.group(1)
                    else:
                        self.__pollutantDatum = ''
                        #print 'Error parsing pollutant datum: "' + self.__pollutantDatum + '"\n'
                    
                    if (self.__pollutantDatum == 'S.D.'):
                        # this should never happen. We are using regular expressions!!
                        self.__pollutantDatum = ''
                        print 'Error in regular expression!'
                    
                    self.m_pollutants[self.__pollutantName] = self.__pollutantDatum.replace(",", ".")
                    
                else:
                    print 'Error parsing pollutant name: "' + self.__pollutantName + '"\n'

                self.__pollutantDatum = ''
                self.__pollutantName = ''
            
        elif (tag == 'font'):
            if (self.__tableCount == 4):
                self.__pollutantRow = False
        elif (tag == 'td'):
            if (self.__td_sampletime):
                self.__td_sampletime = False
        
    def handle_data(self, data):
        if (self.__pollutantRow):
            self.__pollutantName += data
        elif (self.__tableCount == 5 and self.__pollutantName != ''):
            self.__pollutantDatum += data
        elif (self.__td_sampletime):
            result = self.__datetimeRegex.search(data)
            if (result != None):
                nMonth = 0
                if (result.group(2).upper() == 'ENERO'):
                    nMonth = 1
                elif (result.group(2).upper() == 'FEBRERO'):
                    nMonth = 2
                elif (result.group(2).upper() == 'MARZO'):
                    nMonth = 3
                elif (result.group(2).upper() == 'ABRIL'):
                    nMonth = 4
                elif (result.group(2).upper() == 'MAYO'):
                    nMonth = 5
                elif (result.group(2).upper() == 'JUNIO'):
                    nMonth = 6
                elif (result.group(2).upper() == 'JULIO'):
                    nMonth = 7
                elif (result.group(2).upper() == 'AGOSTO'):
                    nMonth = 8
                elif (result.group(2).upper() == 'SEPTIEMBRE'):
                    nMonth = 9
                elif (result.group(2).upper() == 'OCTUBRE'):
                    nMonth = 10
                elif (result.group(2).upper() == 'NOVIEMBRE'):
                    nMonth = 11
                elif (result.group(2).upper() == 'DICIEMBRE'):
                    nMonth = 12
                else:
                    print "Error parsing date: Incorrect month " + result.group(2)
                
                if (nMonth > 0):
                    madrid = pytz.timezone('Europe/Madrid')
                    self.m_sampleTime = madrid.localize(datetime(
                        year = int(result.group(3)),
                        month = nMonth,
                        day = int(result.group(1)),
                        hour=int(result.group(4)),
                        minute=int(result.group(5)),
                        second=0, 
                        microsecond=0))
                else:
                    self.m_sampleTime = None



class  AirecantabriaHTMLParser(HTMLParser):
    """
    HTML parser for probes shown in airecantabria.com
    """
    
    DATA_TYPE_NONE = 0
    DATA_TYPE_POLLUTANTS = 1
    DATA_TYPE_WEATHER = 2

    def __init__(self):
        # call the parent constructor first
        HTMLParser.__init__(self)
        self.__initiliaseParser()
        
        # regex to parse time
        self.__datetimeRegex = re.compile('.* ([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)')

    def __initiliaseParser(self):
        # private data members to parse the HTML entry 
        self.__dataTable = False
        self.__dataType = self.DATA_TYPE_NONE
        self.__thDataType = False
        self.__tdDataParam = False
        self.__tdDataValue = False
        self.__tdDate = False
        self.__currentParam = ''
        self.__currentValue = ''
        # member variables
        self.m_sampleTime = None
        try:
            self.m_pollutants.clear()
        except AttributeError:
            self.m_pollutants = {} # empty dict
        try:
            self.m_weatherParams.clear()
        except AttributeError:
            self.m_weatherParams = {} # empty dict
        
    def reset(self):
        # reset all object's attributes
        self.__initiliaseParser()
        # call the parent reset too
        HTMLParser.reset(self)
    
    def handle_starttag(self, tag, attrs):
        if (tag == 'table'):
            dattrs = dict(attrs)
            if ('class' in dattrs and dattrs['class'] == 'data-table'):
                self.__dataTable = True
        elif (tag == 'th' and self.__dataTable):
            dattrs = dict(attrs)
            if ('colspan' in dattrs and dattrs['colspan'] == '3'):
                self.__thDataType = True
        if (tag == 'td'):
            if (self.__dataTable and self.__dataType != self.DATA_TYPE_NONE):
                if (self.__tdDataParam):
                    self.__tdDataValue = True
                else:
                    self.__tdDataParam = True
            elif (self.__dataTable == False):
                dattrs = dict(attrs)
                if ('colspan' in dattrs and dattrs['colspan'] == '3'):
                    self.__tdDate = True

    def handle_endtag(self, tag):
        if (tag == 'table' and self.__dataTable):
            self.__dataTable = False
            self.__dataType = self.DATA_TYPE_NONE
        if (tag == 'th' and self.__thDataType):
            self.__thDataType = False
        elif (tag == 'td'): 
            if (self.__dataTable and self.__tdDataParam and self.__tdDataValue):
                if (self.__dataType == self.DATA_TYPE_POLLUTANTS):
                    try:
                        self.m_pollutants[self.__currentParam] = float(self.__currentValue)
                    except ValueError:
                        self.m_pollutants[self.__currentParam] = '' # no data available
                elif (self.__dataType == self.DATA_TYPE_WEATHER):
                    try:
                        self.m_weatherParams[self.__currentParam] = self.__currentValue
                    except ValueError:
                        self.m_weatherParams[self.__currentParam] = '' # no data available
                else:
                    print 'Error. This is not a pollutant or a weather parameter:'
                    print '    ' + self.__currentParam + ' - ' + self.__currentValue
                    
                self.__tdDataParam = False
                self.__tdDataValue = False
                self.__currentParam = ''
                self.__currentValue = ''
            if (self.__tdDate):
                self.__tdDate = False

    def handle_data(self, data):
        if (self.__thDataType):
            if (data == 'Contaminantes'):
                self.__dataType = self.DATA_TYPE_POLLUTANTS
            elif (data == 'Meteorolog'):
                self.__dataType = self.DATA_TYPE_WEATHER
        elif (self.__tdDataParam):
            if (self.__currentParam == ''):
                self.__currentParam = data.strip()
            elif (self.__tdDataValue and self.__currentValue == ''):
                self.__currentValue = data.strip()
        elif (self.__tdDate):
            result = self.__datetimeRegex.search(data)
            if (result != None):
                utc = pytz.utc
                self.m_sampleTime = utc.localize(datetime(
                        year = int(result.group(3)),
                        month = int(result.group(2)),
                        day = int(result.group(1)),
                        hour=int(result.group(4)),
                        minute=int(result.group(5)),
                        second=0, 
                        microsecond=0))
            else:
                print "Error parsing sample time"



class  AragonaireHTMLParser(HTMLParser):
    """
    HTML parser for probes shown in airecantabria.com
    """
    
    # constants
    SO2_STR = u'Dióxido de azufre'
    NO2_STR = u'Dióxido de nitrógeno'
    CO_STR = u'Monóxido de carbono'
    O3_STR = u'Ozono'
    
    def __init__(self):
        # call the parent constructor first
        HTMLParser.__init__(self)
        self.__initiliaseParser()
        
        # regex to parse time
        self.__datetimeRegex = re.compile('Actualizado ([0-9]+)/([0-9]+)/([0-9]+) ([0-9]+)h')

    def __initiliaseParser(self):
        # private data members to parse the HTML entry
        self.__dataTable = False
        self.__trData = False
        self.__tdCount = 0
        self.__tdDataFound = False
        self.__tdNoData = False
        self.__currentPollutant = ''
        self.__strongOutOfDataTable = False
        # member variables
        self.m_sampleTime = None
        try:
            self.m_pollutants.clear()
        except AttributeError:
            self.m_pollutants = {} # empty dict
        
    def reset(self):
        # reset all object's attributes
        self.__initiliaseParser()
        # call the parent reset too
        HTMLParser.reset(self)
    
    def handle_starttag(self, tag, attrs):   
        if (tag == 'table'):
            dattrs = dict(attrs)
            if (('class' in dattrs and dattrs['class'] == 'table_data') and
                ('cellspacing' in dattrs and dattrs['cellspacing'] == '0') and
                ('cellpadding' in dattrs and dattrs['cellpadding'] == '5') and
                ('width' in dattrs and dattrs['width'] =='100%') and
                ('border' in dattrs and dattrs['border'] == '0')):
                self.__dataTable = True
        if (tag == 'tr'):
            self.__trData = True                
        if (tag == 'td' and self.__trData):
            self.__tdCount = self.__tdCount + 1
            dattrs = dict(attrs)
            if ('colspan' in dattrs and dattrs['colspan'] == '4'):
                self.__tdNoData = True
        if (tag == 'strong' and self.__dataTable == False):
            self.__strongOutOfDataTable = True

    def handle_endtag(self, tag):
        if (tag == 'table' and self.__dataTable):
            self.__dataTable = False
        elif (tag == 'tr'):
            self.__trData = False
            self.__tdCount = 0
        elif (tag == 'td'):
            self.__tdDataFound = False
            self.__tdNoData = False
        elif (tag == 'strong' and self.__strongOutOfDataTable):
            self.__strongOutOfDataTable = False

    def handle_data(self, data):
        if (self.__tdCount == 1 and self.__tdDataFound == False):
            if (data.decode("utf-8").startswith(self.SO2_STR)):
                self.__currentPollutant = 'SO2'
            elif (data.decode('utf-8').startswith(self.NO2_STR)):
                self.__currentPollutant = 'NO2'
            elif (data.decode('utf-8').startswith(self.CO_STR)):
                self.__currentPollutant = 'CO'
            elif (data.decode('utf-8').startswith(self.O3_STR)):
                self.__currentPollutant = 'O3'
            else:
                print 'Error retrieving pollutant name: ' + data

            self.__tdDataFound = True
        elif (self.__tdCount == 4 and self.__tdDataFound == False):
            if (self.__currentPollutant != ''):
                self.m_pollutants[self.__currentPollutant] = data
                self.__currentPollutant = ''
            self.__tdDataFound = True
        elif (self.__tdCount == 2 and self.__tdNoData):
            if (self.__currentPollutant != ''):
                self.m_pollutants[self.__currentPollutant] = ''
                self.__currentPollutant = ''
            self.__tdDataFound = True
        elif (self.__strongOutOfDataTable):
            result = self.__datetimeRegex.search(data)
            if (result != None):
                madrid = pytz.timezone('Europe/Madrid')
                self.m_sampleTime = madrid.localize(datetime(
                        year = int(result.group(3)),
                        month = int(result.group(2)),
                        day = int(result.group(1)),
                        hour=int(result.group(4)),
                        minute=0,
                        second=0, 
                        microsecond=0))

