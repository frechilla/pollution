﻿# -*- coding: utf-8 -*-

###############
## CONSTANTS ##

# munimadrid.es
#     live feed URL in munimadrid.es. All probes are listed together (thank god for that)
#
MUNIMADRID_DOT_ES_PROBE_URL = \
    'http://www.mambiente.munimadrid.es/opencms/opencms/calaire/consulta/Gases_y_particulas/informegaseshorarios.html'
MUNIMADRID_DOT_ES_SANCHINARRO_LAT = 40.494194 # 40º29'39,1"N
MUNIMADRID_DOT_ES_SANCHINARRO_LON = -3.6605 # 3º39'37,8"W
MUNIMADRID_DOT_ES_PARDO_LAT = 40.518056 # 40º31'5"N
MUNIMADRID_DOT_ES_PARDO_LON = -3.774611 # 3º46'28,6"W 
MUNIMADRID_DOT_ES_TRESOLIVOS_LAT = 40.500556 # 40º30'02"N
MUNIMADRID_DOT_ES_TRESOLIVOS_LON = -3.689722 # 3º41'23"W
MUNIMADRID_DOT_ES_PILAR_LAT = 40.478228 # 40º28'41,62"N 
MUNIMADRID_DOT_ES_PILAR_LON = -3.711542 # 3º42'41,55"W 
MUNIMADRID_DOT_ES_PZACASTILLA_LAT = 40.465556 # 40º27'56"N 
MUNIMADRID_DOT_ES_PZACASTILLA_LON = -3.688611 # 03º41'19"W 
MUNIMADRID_DOT_ES_JUANCARLOSI_LAT = 40.465 # 40º27'54"N 
MUNIMADRID_DOT_ES_JUANCARLOSI_LON = -3.608889 # 03º36'32"W 
MUNIMADRID_DOT_ES_BARAJASPUEBLO_LAT = 40.476928 # 40º28'36,94"N 
MUNIMADRID_DOT_ES_BARAJASPUEBLO_LON = -3.580028 # 03º34'48,10"W 
MUNIMADRID_DOT_ES_URBEMBAJADA_LAT = 40.4625 # 40º27'45"N 
MUNIMADRID_DOT_ES_URBEMBAJADA_LON = -3.580556 # 03º34'50"W 
MUNIMADRID_DOT_ES_RAMONYCAJAL_LAT = 40.451472 # 40º27'05,30"N 
MUNIMADRID_DOT_ES_RAMONYCAJAL_LON = -3.677353 # 3º40'38,47"W 
MUNIMADRID_DOT_ES_CUATROCAMINOS_LAT = 40.445542 # 40º26'43,95"N 
MUNIMADRID_DOT_ES_CUATROCAMINOS_LON = -3.707128 # 3º42'25,66"W 
MUNIMADRID_DOT_ES_CASTELLANA_LAT = 40.439722 # 40º26'23"N 
MUNIMADRID_DOT_ES_CASTELLANA_LON = -3.690278 # 3º41'25"W 
MUNIMADRID_DOT_ES_ARTUROSORIA_LAT = 40.440047 # 40º26'24,17"N 
MUNIMADRID_DOT_ES_ARTUROSORIA_LON = -3.639233 # 3º38'21,24"W 
MUNIMADRID_DOT_ES_CASADECAMPO_LAT = 40.419356 # 40º25'09,68"N 
MUNIMADRID_DOT_ES_CASADECAMPO_LON = -3.747344 # 3º44'50,44"W 
MUNIMADRID_DOT_ES_PZAESPANA_LAT = 40.423992 # 40º25'26,37"N 
MUNIMADRID_DOT_ES_PZAESPANA_LON = -3.712333 # 3º42'44,40"W 
MUNIMADRID_DOT_ES_PZACARMEN_LAT = 40.419208 # 40º25'09,15"N 
MUNIMADRID_DOT_ES_PZACARMEN_LON = -3.703172 # 3º42'11,42"W 
MUNIMADRID_DOT_ES_ESCUELASAGUIRRE_LAT = 40.421564 # 40º25'17,63"N 
MUNIMADRID_DOT_ES_ESCUELASAGUIRRE_LON = -3.682319 # 3º40'56,35"W 
MUNIMADRID_DOT_ES_RETIRO_LAT = 40.414444 # 40º24'52"N 
MUNIMADRID_DOT_ES_RETIRO_LON = -3.6825 # 3º40'57"W 
MUNIMADRID_DOT_ES_MORATALAZ_LAT = 40.407956 # 40º24'28,64"N 
MUNIMADRID_DOT_ES_MORATALAZ_LON = -3.645294 # 3º38'43,06"W 
MUNIMADRID_DOT_ES_FAROLILLO_LAT = 40.394778 # 40º23'41,20"N 
MUNIMADRID_DOT_ES_FAROLILLO_LON = -3.731833 # 3º43'54,60"W 
MUNIMADRID_DOT_ES_FDEZLADREDA_LAT = 40.384722 # 40º23'05"N 
MUNIMADRID_DOT_ES_FDEZLADREDA_LON = -3.718611 # 3º43'7"W 
MUNIMADRID_DOT_ES_MENDEZALVARO_LAT = 40.398056 # 40º23'53"N 
MUNIMADRID_DOT_ES_MENDEZALVARO_LON = -3.686667 # 3º41'12"W 
MUNIMADRID_DOT_ES_VALLECAS_LAT = 40.38815 # 40º23'17,34"N 
MUNIMADRID_DOT_ES_VALLECAS_LON = -3.651522 # 3º39'05,48"W 
MUNIMADRID_DOT_ES_ENSANCHEVALLECAS_LAT = 40.372988 # 40º22'22"N (moved a bit)
MUNIMADRID_DOT_ES_ENSANCHEVALLECAS_LON = -3.612094 # 3º36'43"W
MUNIMADRID_DOT_ES_VILLAVERDE_LAT = 40.3471 # 40º20'49,56"N
MUNIMADRID_DOT_ES_VILLAVERDE_LON = -3.713328 # 3º42'47,98"W 


# madrid.org
#   List of probes: http://gestiona.madrid.org/azul_internet/html/web/DatosRedAccion.icm?ESTADO_MENU=2_1
#
# 02 corredor del henares
MADRID_DOT_ORG_PROBE_ALCALA_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=3'  # Alcala de Henares
MADRID_DOT_ORG_PROBE_ALCALA_LAT = 40.479323 # 40º28'45"N (moved a small bit)
MADRID_DOT_ORG_PROBE_ALCALA_LON = -3.377957 # 03º22'40"W

MADRID_DOT_ORG_PROBE_ALCOBENDAS_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=4'  # Alcobendas
MADRID_DOT_ORG_PROBE_ALCOBENDAS_LAT = 40.540502 # 40º32'26"N (moved a small bit)
MADRID_DOT_ORG_PROBE_ALCOBENDAS_LON = -3.645191 # 03º38'41"W

MADRID_DOT_ORG_PROBE_TORREJON_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=7'  # Torrejon de Ardoz
MADRID_DOT_ORG_PROBE_TORREJON_LAT = 40.449543 # 40º27'00"N (moved)
MADRID_DOT_ORG_PROBE_TORREJON_LON = -3.477649 # 03º29'03"W

MADRID_DOT_ORG_PROBE_COSLADA_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=9'  # Coslada
MADRID_DOT_ORG_PROBE_COSLADA_LAT = 40.430979 # 40º25'52"N (moved to Avda. José Gárate)
MADRID_DOT_ORG_PROBE_COSLADA_LON = -3.542812 # 03º33'34"W 

MADRID_DOT_ORG_PROBE_ARGANDA_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=15' # Arganda del rey
MADRID_DOT_ORG_PROBE_ARGANDA_LAT = 40.300789 # 40º18'35"N (moved to C/Rio Tajuña)
MADRID_DOT_ORG_PROBE_ARGANDA_LON = -3.458902 # 03º27'31"W 

MADRID_DOT_ORG_PROBE_RIVAS_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=18' # Rivas vaciamadrid
MADRID_DOT_ORG_PROBE_RIVAS_LAT = 40.360076 # 40º21'36"N (adjusted a small bit)
MADRID_DOT_ORG_PROBE_RIVAS_LON = -3.542492 # 3º32'32"W 

MADRID_DOT_ORG_PROBE_ALGETE_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=20' # Algete
MADRID_DOT_ORG_PROBE_ALGETE_LAT = 40.599727 # 40º35'59"N (moved to Parque Europa, Algete)
MADRID_DOT_ORG_PROBE_ALGETE_LON = -3.503282 # 03º30'11"W
    
#
# 03 urbana sur
MADRID_DOT_ORG_PROBE_GETAFE_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=1'  # Getafe
MADRID_DOT_ORG_PROBE_GETAFE_LAT = 40.324664 # 40º18'35"N (moved to Avd. Teresa Calcuta)
MADRID_DOT_ORG_PROBE_GETAFE_LON = -3.714113 # 03º44'09"W 

MADRID_DOT_ORG_PROBE_LEGANES_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=2'  # Leganes
MADRID_DOT_ORG_PROBE_LEGANES_LAT = 40.339756 # 40º18'35"N (moved to C/ Roncal)
MADRID_DOT_ORG_PROBE_LEGANES_LON = -3.754516 # 03º45'16"W 

MADRID_DOT_ORG_PROBE_FUENLABRADA_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=5'  # Fuenlabrada
MADRID_DOT_ORG_PROBE_FUENLABRADA_LAT = 40.281512 # 40º16'52"N  (moved to C/ Grecia)
MADRID_DOT_ORG_PROBE_FUENLABRADA_LON = -3.800959 # 03º48'06"W 

MADRID_DOT_ORG_PROBE_MOSTOLES_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=6'  # Mostoles
MADRID_DOT_ORG_PROBE_MOSTOLES_LAT = 40.324251 # 40º19'27"N (moved to Parque Liana)
MADRID_DOT_ORG_PROBE_MOSTOLES_LON = -3.876767 # 03º52'35"W 

MADRID_DOT_ORG_PROBE_ALCORCON_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=8'  # Alcorcon
MADRID_DOT_ORG_PROBE_ALCORCON_LAT = 40.342061 # 40º20'30"N (moved to Avda del Oeste, Colegio Blas de Otero)
MADRID_DOT_ORG_PROBE_ALCORCON_LON = -3.833679 # 03º50'1.5"W

MADRID_DOT_ORG_PROBE_ARANJUEZ_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=13' # Aranjuez
MADRID_DOT_ORG_PROBE_ARANJUEZ_LAT = 40.03321 # 40º02'09"N (adjusted to C/Moreras)
MADRID_DOT_ORG_PROBE_ARANJUEZ_LON = -3.591414 # 03º35'31"W

MADRID_DOT_ORG_PROBE_VALDEMORO_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=21' # Valdemoro
MADRID_DOT_ORG_PROBE_VALDEMORO_LAT = 40.185278 # 40º11'07"N (no need to move)
MADRID_DOT_ORG_PROBE_VALDEMORO_LON = -3.680278 # 03º40'49"W

#
# 04 urbana noroeste
MADRID_DOT_ORG_PROBE_COLMENAR_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=11' # Colmenar Viejo
MADRID_DOT_ORG_PROBE_COLMENAR_LAT = 40.66462 # 40º39'58"N (adjusted a small bit)
MADRID_DOT_ORG_PROBE_COLMENAR_LON = -3.773871 # 03º46'22"W

MADRID_DOT_ORG_PROBE_MAJADAHONDA_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=12' # Majadahonda
MADRID_DOT_ORG_PROBE_MAJADAHONDA_LAT = 40.446244 # 40º26'51"N (moved to C/ Isaac Albéniz)
MADRID_DOT_ORG_PROBE_MAJADAHONDA_LON = -3.869012 # 03º52'04"W

MADRID_DOT_ORG_PROBE_COLLADO_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=14' # Collado Villalba
MADRID_DOT_ORG_PROBE_COLLADO_LAT = 40.633398 # 40º18'02"N (re-adjusted to C/Cañada Real)
MADRID_DOT_ORG_PROBE_COLLADO_LON = -4.013038 # 04º00'48"W

#
# 05 rural sierra norte
MADRID_DOT_ORG_PROBE_GUADALIX_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=19' # Guadalix de la Sierra
MADRID_DOT_ORG_PROBE_GUADALIX_LAT = 40.780833 # 40º46'51"N (no need to move)
MADRID_DOT_ORG_PROBE_GUADALIX_LON = -3.7025 # 03º42'09"W

MADRID_DOT_ORG_PROBE_ATAZAR_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=22' # El Atazar
MADRID_DOT_ORG_PROBE_ATAZAR_LAT = 40.910278 # 40º54'37"N (Approximately well-located. Can't do better)
MADRID_DOT_ORG_PROBE_ATAZAR_LON = -3.466667 # 03º27'60"W 

#
# 06 cuenca del Alberche
MADRID_DOT_ORG_PROBE_SANMARTIN_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=17' # San Martin de Valdeiglesias
MADRID_DOT_ORG_PROBE_SANMARTIN_LAT = 40.365986 # 40º23'8"N (moved approximately to here: http://gestiona.madrid.org/ICMdownload/m17.jpg)
MADRID_DOT_ORG_PROBE_SANMARTIN_LON = -4.340952 # 04º23'48"W 

MADRID_DOT_ORG_PROBE_ELPRADO_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=23' # Villa del Prado
MADRID_DOT_ORG_PROBE_ELPRADO_LAT = 40.252 # 40º15'07"N (moved near the "Virgen de la Poveda" hospital)
MADRID_DOT_ORG_PROBE_ELPRADO_LON = -4.274793 # 03º16'26"W (see http://gestiona.madrid.org/ICMdownload/m23.jpg)

#
# 07 Cuenca del tajunna
MADRID_DOT_ORG_PROBE_VILLAREJO_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=16' # Villarejo de Salvanes
MADRID_DOT_ORG_PROBE_VILLAREJO_LAT = 40.166944 # 40º10'01"N (no need to move)
MADRID_DOT_ORG_PROBE_VILLAREJO_LON = -3.276667 # 03º16'36"W  (good enough according to http://gestiona.madrid.org/ICMdownload/m16.jpg)

MADRID_DOT_ORG_PROBE_ORUSCO_URL = \
    'http://gestiona.madrid.org/azul_internet/html/web/DatosEstacionAccion.icm?ESTADO_MENU=2&idEstacion=24' # Orusco de Tajunna
MADRID_DOT_ORG_PROBE_ORUSCO_LAT = 40.286944 # 40º17'13"N (no need to move. "Repetidor de Telefonía")
MADRID_DOT_ORG_PROBE_ORUSCO_LON = -3.222222 # 03º13'20"W (good enough according to http://gestiona.madrid.org/ICMdownload/m24.jpg)


# jccm.es
#   List of probes: http://pagina.jccm.es/medioambiente/rvca/estaciones/caseta/intro_casetas.htm
#
JCCM_ES_PROBE_ALBACETE_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Albacete.htm'
JCCM_ES_PROBE_ALBACETE_LAT = 38.979295 # 38º 58' 54''N (moved a good deal to "calle historia")
JCCM_ES_PROBE_ALBACETE_LON = -1.852133 # 01º 57' 24''W

JCCM_ES_PROBE_AZUQUECA_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Azuqueca.htm'
JCCM_ES_PROBE_AZUQUECA_LAT = 40.570971 # 40º 34' 25''N (moved a bit closer to "calle la flor")
JCCM_ES_PROBE_AZUQUECA_LON = -3.264611 # 03º 15' 48''W

JCCM_ES_PROBE_GUADALAJARA_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Guadalajara.htm'
JCCM_ES_PROBE_GUADALAJARA_LAT = 40.629722 # 40º 37' 47''N (no need to move)
JCCM_ES_PROBE_GUADALAJARA_LON = -3.171667 # 03º 10' 18''W

JCCM_ES_PROBE_TOLEDO_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Toledo.htm'
JCCM_ES_PROBE_TOLEDO_LAT = 39.868056 # 39º 52' 05''N (no need to move)
JCCM_ES_PROBE_TOLEDO_LON = -4.020833 # 04º 01' 15''W

JCCM_ES_PROBE_CIUDADREAL_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Ciudadreal.htm'
JCCM_ES_PROBE_CIUDADREAL_LAT = 38.993889 # 38º 59' 38''N (no need to move)
JCCM_ES_PROBE_CIUDADREAL_LON = -3.937778 # 03º 56' 16''W

JCCM_ES_PROBE_CUENCA_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Cuenca.htm'
JCCM_ES_PROBE_CUENCA_LAT = 40.061849 # 40º 03' 43''N (moved a small bit)
JCCM_ES_PROBE_CUENCA_LON = -2.129712 # 02º 07' 46''W

JCCM_ES_PROBE_ILLESCAS_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Illescas.htm'
JCCM_ES_PROBE_ILLESCAS_LAT = 40.119167 # 40º 07' 09''N (Left where the website says. Looks close enough)
JCCM_ES_PROBE_ILLESCAS_LON = -3.833056 # 03º 49' 59''W

#TODO have a look at this probe. Where is it exactly??
JCCM_ES_PROBE_TALAVERA_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Talavera.htm'
JCCM_ES_PROBE_TALAVERA_LAT = 39.958056 # 39º 57' 29''N (Can't find it. Left at the same spot the website says)
JCCM_ES_PROBE_TALAVERA_LON = -4.850833 # 04º 51' 03''W

JCCM_ES_PROBE_PUERTOLLANO_CALLEANCHA_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Cancha.htm'
JCCM_ES_PROBE_PUERTOLLANO_CALLEANCHA_LAT = 38.689333 # 38º 41' 28''N (moved closer to "seguridad social") 
JCCM_ES_PROBE_PUERTOLLANO_CALLEANCHA_LON = -4.111505 # 04º 06' 35''W

JCCM_ES_PROBE_PUERTOLLANO_INSTITUTO_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Instituto.htm'
JCCM_ES_PROBE_PUERTOLLANO_INSTITUTO_LAT = 38.680702 # 38º 40' 54''N (moved closer to the high school)
JCCM_ES_PROBE_PUERTOLLANO_INSTITUTO_LON = -4.108297 # 04º 06' 25''W

#TODO have a look at this probe. Where is it exactly??
JCCM_ES_PROBE_PUERTOLLANO_CAMPOFUTBOL_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/Cfutbol.htm'
JCCM_ES_PROBE_PUERTOLLANO_CAMPOFUTBOL_LAT = 38.684444 # 38º 41' 04''N (Can't find it. Left at the same spot the website says)
JCCM_ES_PROBE_PUERTOLLANO_CAMPOFUTBOL_LON = -4.088611 # 04º 05' 19''W

#TODO have a look at this probe. Where is it exactly??
JCCM_ES_PROBE_PUERTOLLANO_B630_URL = 'http://pagina.jccm.es/medioambiente/rvca/Dest/B630.htm'
JCCM_ES_PROBE_PUERTOLLANO_B630_LAT = 38.703611 # 38º 42' 13''N (Can't find it. Left at the same spot the website says)
JCCM_ES_PROBE_PUERTOLLANO_B630_LON = -4.110278 # 04º 06' 37''W


# http://www.airecantabria.com/
#   List of probes: http://www.airecantabria.com/estaciones.php
#
AIRECANTABRIA_COM_PROBE_SANTANDER_CENTRO_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=6'
AIRECANTABRIA_COM_PROBE_SANTANDER_CENTRO_LAT = 43.461424962581 # UTM X = 434571, Y = 4812375
AIRECANTABRIA_COM_PROBE_SANTANDER_CENTRO_LON = -3.808804621545313

AIRECANTABRIA_COM_PROBE_SANTANDER_TETUAN_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=7'
AIRECANTABRIA_COM_PROBE_SANTANDER_TETUAN_LAT = 43.46854114885479 # UTM X = 436069, Y = 4813151
AIRECANTABRIA_COM_PROBE_SANTANDER_TETUAN_LON = -3.790379781321349

AIRECANTABRIA_COM_PROBE_CAMARGO_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=5'
AIRECANTABRIA_COM_PROBE_CAMARGO_LAT = 43.421636099303996 # UTM X = 431916, Y = 4807982
AIRECANTABRIA_COM_PROBE_CAMARGO_LON = -3.841073037382859

AIRECANTABRIA_COM_PROBE_GUARNIZO_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=4'
AIRECANTABRIA_COM_PROBE_GUARNIZO_LAT = 43.40712535835906 # UTM X = 432146, Y = 4806368
AIRECANTABRIA_COM_PROBE_GUARNIZO_LON = -3.8380316198472606

AIRECANTABRIA_COM_PROBE_TORRELAVEGA_MINAS_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=1'
AIRECANTABRIA_COM_PROBE_TORRELAVEGA_MINAS_LAT = 43.35669590571541 # UTM X = 414106, Y = 4800972
AIRECANTABRIA_COM_PROBE_TORRELAVEGA_MINAS_LON = -4.059954535886294

AIRECANTABRIA_COM_PROBE_TORRELAVEGA_ZAPATON_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=2'
AIRECANTABRIA_COM_PROBE_TORRELAVEGA_ZAPATON_LAT = 43.346972994861844 # UTM X = 414900, Y = 4799882
AIRECANTABRIA_COM_PROBE_TORRELAVEGA_ZAPATON_LON = -4.049988784700798

AIRECANTABRIA_COM_PROBE_TORRELAVEGA_BARREDA_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=3'
AIRECANTABRIA_COM_PROBE_TORRELAVEGA_BARREDA_LAT = 43.36375662731612 # UTM X = 415316, Y = 4801741
AIRECANTABRIA_COM_PROBE_TORRELAVEGA_BARREDA_LON = -4.045144118311133

AIRECANTABRIA_COM_PROBE_TORRELAVEGA_CIMA_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=10'
AIRECANTABRIA_COM_PROBE_TORRELAVEGA_CIMA_LAT = 43.35744160042185 # UTM X = 414566, Y = 4801049
AIRECANTABRIA_COM_PROBE_TORRELAVEGA_CIMA_LON = -4.0542909645812895

AIRECANTABRIA_COM_PROBE_BUELNA_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=11'
AIRECANTABRIA_COM_PROBE_BUELNA_LAT = 43.26527397276361 # UTM X = 413748, Y = 4790822
AIRECANTABRIA_COM_PROBE_BUELNA_LON = -4.062777985642403

AIRECANTABRIA_COM_PROBE_REINOSA_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=8'
AIRECANTABRIA_COM_PROBE_REINOSA_LAT = 43.00197635629765 # UTM X = 407434, Y = 4761660
AIRECANTABRIA_COM_PROBE_REINOSA_LON = -4.135693847571788

AIRECANTABRIA_COM_PROBE_TOJOS_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=9'
AIRECANTABRIA_COM_PROBE_TOJOS_LAT = 43.15441856159531 # UTM X = 397786, Y = 4778730
AIRECANTABRIA_COM_PROBE_TOJOS_LON = -4.257177163092484

AIRECANTABRIA_COM_PROBE_CASTRO_URL = 'http://www.airecantabria.com/estaciones-ahora.php?ides=12'
AIRECANTABRIA_COM_PROBE_CASTRO_LAT = 43.383229180627644 # UTM X = 482057, Y = 4803397
AIRECANTABRIA_COM_PROBE_CASTRO_LON = -3.221518592956929


# http://www.aragonaire.es/index.php
#   List of probes: http://www.aragonaire.es/site_information.php
#
ARAGONAIRE_ES_PROBE_ALAGON_URL = 'http://www.aragonaire.es/ajax_process/show_site_tabs.php?doajax=true&site_id=50008001&t_action=data&pref=undefined'
ARAGONAIRE_ES_PROBE_ALAGON_LAT = 41.762073
ARAGONAIRE_ES_PROBE_ALAGON_LON = -1.144798

ARAGONAIRE_ES_PROBE_BUJARALOZ_URL = 'http://www.aragonaire.es/ajax_process/show_site_tabs.php?doajax=true&site_id=50059001&t_action=data&pref=undefined'
ARAGONAIRE_ES_PROBE_BUJARALOZ_LAT = 41.504788
ARAGONAIRE_ES_PROBE_BUJARALOZ_LON = -0.153154

ARAGONAIRE_ES_PROBE_HUESCA_URL = 'http://www.aragonaire.es/ajax_process/show_site_tabs.php?doajax=true&site_id=22125001&t_action=data&pref=undefined'
ARAGONAIRE_ES_PROBE_HUESCA_LAT = 42.134349
ARAGONAIRE_ES_PROBE_HUESCA_LON = -0.404224

ARAGONAIRE_ES_PROBE_MONZON_URL = 'http://www.aragonaire.es/ajax_process/show_site_tabs.php?doajax=true&site_id=22158001&t_action=data&pref=undefined'
ARAGONAIRE_ES_PROBE_MONZON_LAT = 41.918113
ARAGONAIRE_ES_PROBE_MONZON_LON = 0.195838

ARAGONAIRE_ES_PROBE_TERUEL_URL = 'http://www.aragonaire.es/ajax_process/show_site_tabs.php?doajax=true&site_id=44216001&t_action=data&pref=undefined'
ARAGONAIRE_ES_PROBE_TERUEL_LAT = 40.336420
ARAGONAIRE_ES_PROBE_TERUEL_LON = -1.108396

ARAGONAIRE_ES_PROBE_TORRELISA_URL = 'http://www.aragonaire.es/ajax_process/show_site_tabs.php?doajax=true&site_id=22190001&t_action=data&pref=undefined'
ARAGONAIRE_ES_PROBE_TORRELISA_LAT = 42.457644
ARAGONAIRE_ES_PROBE_TORRELISA_LON = 0.182025


# http://www.asturias.es/portal/site/medioambiente/
#   List of probes: http://www.asturias.es/portal/site/medioambiente/menuitem.a19f58541256a36dc998e810a6108a0c/?vgnextoid=3b195b51cb90c110VgnVCM1000006a01a8c0RCRD&i18n.http.lang=es
#
ASTURIAS_ES_PROBE_AVILES_LLANOPONTE_LAT = 43.552778 # 43°33'10"N
ASTURIAS_ES_PROBE_AVILES_LLANOPONTE_LON = -5.916111 # 5°54'58"W

ASTURIAS_ES_PROBE_AVILES_PZAGUITARRA_LAT = 43.56 # 43°33'36"N
ASTURIAS_ES_PROBE_AVILES_PZAGUITARRA_LON = -5.926111 # 5°55'34"W

ASTURIAS_ES_PROBE_AVILES_MATADERO_LAT = 43.584167 # 43°35'03"N
ASTURIAS_ES_PROBE_AVILES_MATADERO_LON = -5.918056 # 5°55'05"W

ASTURIAS_ES_PROBE_AVILES_LLARANES_LAT = 43.551111 # 43°33'04"N
ASTURIAS_ES_PROBE_AVILES_LLARANES_LON = -5.896944 # 5°53'49"W

ASTURIAS_ES_PROBE_GIJON_CASTILLA_LAT = 43.541667 # 43°32'30"N
ASTURIAS_ES_PROBE_GIJON_CASTILLA_LON = -5.65 # 5°39'00"W

ASTURIAS_ES_PROBE_GIJON_ARGENTINA_LAT = 43.539444 # 43°32'22"N
ASTURIAS_ES_PROBE_GIJON_ARGENTINA_LON = -5.7 # 5°42'00"W

ASTURIAS_ES_PROBE_GIJON_CONSTITUTION_LAT = 43.531111 # 43°31'52"N
ASTURIAS_ES_PROBE_GIJON_CONSTITUCION_LON = -5.671667 # 5°40'18"W

ASTURIAS_ES_PROBE_GIJON_MONTEVIL_LAT = 43.584167 # 43°35'03"N
ASTURIAS_ES_PROBE_GIJON_MONTEVIL_LON = -5.918056 # 5°55'05"W

ASTURIAS_ES_PROBE_GIJON_HFELGUEROSO_LAT = 43.536389 # 43°32'11"N
ASTURIAS_ES_PROBE_GIJON_HFELGUEROSO_LON = -5.6575 # 5°39'27"W

ASTURIAS_ES_PROBE_LANGREO_FELGUERA_LAT = 43.309722 # 43°18'35"N
ASTURIAS_ES_PROBE_LANGREO_FELGUERA_LON = -5.691111 # 5°41'28"W

ASTURIAS_ES_PROBE_LANGREO_MERINAN_LAT = 43.309167 # 43°18'33"N
ASTURIAS_ES_PROBE_LANGREO_MERINAN_LON = -5.705833 # 5°42'21"W

ASTURIAS_ES_PROBE_LANGREO_SAMA_LAT = 43.296944 # 43°17'49"N
ASTURIAS_ES_PROBE_LANGREO_SAMA_LON = -5.683333 # 5°41'00"W

ASTURIAS_ES_PROBE_SMARTIN_FLORAN_LAT = 43.288889 # 43°17'20"N
ASTURIAS_ES_PROBE_SMARTIN_FLORAN_LON = -5.644444 # 5°38'40"W

ASTURIAS_ES_PROBE_MIERES_LAT = 43.2575 # 43°15'27"N
ASTURIAS_ES_PROBE_MIERES_LON = -5.774722 # 5°46'29"W

ASTURIAS_ES_PROBE_OVIEDO_TRUBIA_LAT = 43.343611 # 43°20'37"N
ASTURIAS_ES_PROBE_OVIEDO_TRUBIA_LON = -5.984167 # 5°59'03"W

ASTURIAS_ES_PROBE_OVIEDO_PTOMAS_LAT = 43.373889 # 43°22'26"N
ASTURIAS_ES_PROBE_OVIEDO_PTOMAS_LON = -5.871667 # 5°52'18"W

ASTURIAS_ES_PROBE_OVIEDO_PTOROS_LAT = 43.358611 # 43°21'31"N
ASTURIAS_ES_PROBE_OVIEDO_PTOROS_LON = -5.865278 # 5°51'55"W

ASTURIAS_ES_PROBE_OVIEDO_PDEPORTES_LAT = 43.368333 # 43°22'06"N
ASTURIAS_ES_PROBE_OVIEDO_PDEPORTES_LON = -5.831944 # 5°49'55"W

ASTURIAS_ES_PROBE_LUGONES_LAT = 43.403611 # 43°24'13"N
ASTURIAS_ES_PROBE_LUGONES_LON = -5.810833 # 5°48'39"W

ASTURIAS_ES_PROBE_CANGASNARCEA_LAT = 43.177778 # 43°10'40"N
ASTURIAS_ES_PROBE_CANGASNARCEA_LON = -6.547222 # 6°32'50"W

