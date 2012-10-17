# -*- coding: utf-8 -*-

# timestamp output files
from datetime import datetime

# handling dates to generate timestamps based on UTC
# pytz can be missing. Install it using "easy_install pytz"
import calendar
import pytz
from pytz import timezone

# generating UTF-8 encoded files
import codecs


from probe_parsers import ProbeParser
from probe_parsers import MadridDotOrgLiveProbeParser
from probe_parsers import MunimadridDotEsLiveProbeParser
from probe_parsers import JCCMDotEsLiveProbeParser
from probe_parsers import AirecantabriaLiveProbeParser
from probe_parsers import AragonaireDotEsLiveProbeParser
from probe_parsers import AsturiasDotEsLiveProbeParser

from probe import qairStatus_SO2
from probe import qairStatus_O3
from probe import qairStatus_NO2
from probe import qairStatus_PM10
from probe import qairStatus_CO


# from http://stackoverflow.com/questions/5214866/python-add-date-stamp-to-text-file
def timeStamped(fname, fmt='%Y%m%d-%H%M%S_{fname}'):
    return datetime.now().strftime(fmt).format(fname=fname)

def D_printParam(name, value):
    if (not value is None):
        if (value == ""):
            print "%s: --" % name
        else:
            print "%s: %s" % (name, str(value))

####################
###     MAIN     ###

# list of probe parsers
probe_parser_list = []
probe_parser_list.append(MadridDotOrgLiveProbeParser()) # madrid.org
probe_parser_list.append(MunimadridDotEsLiveProbeParser()) # munimadrid.es
probe_parser_list.append(JCCMDotEsLiveProbeParser()) # jccm.es
probe_parser_list.append(AragonaireDotEsLiveProbeParser()) # aragonaire.es
probe_parser_list.append(AirecantabriaLiveProbeParser()) # airecantabria.com
#probe_parser_list.append(AsturiasDotEsLiveProbeParser())
        
print "Parsing probes..."
for thisProbeParser in probe_parser_list:
    thisProbeParser.update()

print "Generating geojson file..."
with codecs.open(timeStamped('probes.geojson'), 'w', "utf-8") as outf:
    outf.write(u"""{
 "type": "FeatureCollection",
 "features": [
""")
    
    currentId = 0
    for thisProbeParser in probe_parser_list:
        for thisProbe in thisProbeParser.probe_list:
            # geojson needs points to be separated by commas. The latest line
            # must not have a final comma
            if (currentId > 0):
                outf.write(',\n') 

            # Note that python will convert \n to os.linesep
            outf.write('  { "type": "Feature", "id": ' + str(currentId) + 
                ', "properties": {"COD": "p' + str(currentId) + '"' + 
#                ', "REG": "Comunidad de Madrid"' +
                ', "NAME": "' + thisProbe.name + '"');
            if (thisProbe.last_measure.sample_time == None):
                outf.write(', "DATE": 0')
            else:
                outf.write(', "DATE": ' + str(calendar.timegm(thisProbe.last_measure.sample_time.astimezone(pytz.utc).timetuple())))
            outf.write(', "STATUS": {' +
                    '"SO2": '    + str(qairStatus_SO2(thisProbe.last_measure.so2)) +
                    ', "O3": '   + str(qairStatus_O3(thisProbe.last_measure.o3)) +
                    ', "NO2": '  + str(qairStatus_NO2(thisProbe.last_measure.no2)) +
                    ', "PM10": ' + str(qairStatus_PM10(thisProbe.last_measure.pm10)) +
                    ', "CO": '   + str(qairStatus_CO(thisProbe.last_measure.co)) +
                    '} }' +
                ', "geometry": {"type": "Point", "coordinates": [' +
                str(thisProbe.longitude) + ', ' + str(thisProbe.latitude) + ']} }' )
            
            currentId = currentId + 1
            
            print "---------------------------------------"
            print "Station: " + thisProbe.name
            
            if (thisProbe.last_measure.sample_time == None):
                print "Time: --"
            else:
                fmt = '%Y-%m-%d %H:%M:%S %Z%z'
                print "Time: " + thisProbe.last_measure.sample_time.astimezone(timezone('Europe/Madrid')).strftime(fmt)
                #print "    " + str(calendar.timegm(thisProbe.last_measure.sample_time.astimezone(timezone('Europe/Madrid')).timetuple()))
            
            D_printParam("CO", thisProbe.last_measure.co)                    
            D_printParam("NO", thisProbe.last_measure.no)
            D_printParam("NO2", thisProbe.last_measure.no2)
            D_printParam("SO2", thisProbe.last_measure.so2)
            D_printParam("PM25", thisProbe.last_measure.pm25)
            D_printParam("PM10", thisProbe.last_measure.pm10)
            D_printParam("O3", thisProbe.last_measure.o3)
            D_printParam("SH2", thisProbe.last_measure.sh2)
            D_printParam("TOL", thisProbe.last_measure.tol)
            D_printParam("BEN", thisProbe.last_measure.ben)
            D_printParam("XYL", thisProbe.last_measure.xyl)
            
            D_printParam("Wind speed", thisProbe.last_measure.wind_speed)
            D_printParam("Wind dir", thisProbe.last_measure.wind_dir)
            D_printParam("Temp", thisProbe.last_measure.temp)
            D_printParam("Hum", thisProbe.last_measure.hum)
            D_printParam("Pressure", thisProbe.last_measure.pressure)
            D_printParam("Solar radiation", thisProbe.last_measure.solar_rad)
            D_printParam("Precipitation", thisProbe.last_measure.precip)            
            print ""
    else:
        outf.write('\n ]\n')
        outf.write('}\n')

    outf.close()
