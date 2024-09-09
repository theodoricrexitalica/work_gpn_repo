from math import *
from TechlogMath import *
from operator import *
import sys
if sys.version_info[0]==3:
    from six.moves import range

PI     = 3.14159265358979323846
PIO2   = 1.57079632679489661923
PIO4   = 7.85398163397448309616E-1
SQRT2  = 1.41421356237309504880
SQRTH  = 7.07106781186547524401E-1
E      = exp(1)
LN2    = log(2)
LN10   = log(10)
LOG2E  = 1.4426950408889634073599
LOG10E = 1.0 / LN10
MissingValue = -9999
def iif(condition, trueResult=MissingValue, falseResult=MissingValue):
	if condition:
		return trueResult
	else:
		return falseResult

#Declarations
#The dictionary of parameters v2.0
#name,bname,type,family,measurement,unit,value,mode,description,group,min,max,list,enable,iscombocheckbox,isused
parameterDict = {}
try:
	if Parameter:
		pass
except NameError:
	class Parameter:
		def __init__(self, **d):
			pass

__author__ = """Taras DOLGUSHIN (Dolgushin.TYu)"""
__date__ = """2021-08-17"""
__version__ = """1.0"""
__pyVersion__ = """3"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""
__applyMode__ = """0"""
__awiEngine__ = """v2"""
__layoutTemplateMode__ = """"""
__includeMissingValues__ = """True"""
__keepPreviouslyComputedValues__ = """True"""
__areInputDisplayed__ = """True"""
__useMultiWellLayout__ = """True"""
__idForHelp__ = """"""
__executionGranularity__ = """full"""
#DeclarationsEnd
s = ";"
print("Well", s, "Top_K/Bot_K", s,  "Zones")
for well in db.selectedWellList():
	ds = "PT_RIGIS"
	var = "LITH"
	zones = "ZONES_ety_bp16"
	zone_name = "BP16_2_topS"
	title_top = "TOP_K"
	title_bot = "BOT_K"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	lith = db.variableLoad(well, ds, var)
	top_k = []
	indice = db.datasetZoneIndice(well, ds, zones, zone_name, "Zone Name")
	if 1 in lith[indice[0]:indice[1]]:
		for i in range(len(md))[indice[0]:indice[1]]:
		#print("svergu-vniz", md[i])
			if lith[i] == 1 and lith[i-1] != 1:
				top_k.append(md[i])
		bot_k = []

		for i in range(len(md))[indice[1]+10:indice[0]-10:-1]:
			#print("snizu-verh",md[i], lith[i])
			if lith[i-1] == 1 and lith[i] != 1:
				bot_k.append(md[i])
		print(well, s, (top_k)[0], s, "BP16_2_TOP_K")
		print(well, s, (bot_k)[0], s, "BP16_2_BOT_K")
	else:
		pass
