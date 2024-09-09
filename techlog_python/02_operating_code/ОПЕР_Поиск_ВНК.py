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
__date__ = """2021-07-21"""
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
def Heff(well, ds):
	broken_wells_infunction = []
	if db.datasetExists(well, ds):
		db.variableCopy(well, "Index", "TVDSS", ds, "TVDSS", "anti-aliasing", "project", "project", -1 , 0, 1)
		db.variableCopy(well, zonation, "ZONES", ds, "ZONES", "automatic", "project", "project", -1 , 0, 1)
		tvdss = db.variableLoad(well, ds, "TVDSS")
		###Если нет TVDSS в датасете, берем MD###	
		#tvdss = db.variableLoad(well, ds, db.referenceName(well, ds)) 
		satur =  db.variableLoad(well, ds, "satur")
		zones = db.variableLoad(well, ds, "ZONES")
		owc_tvdss = []
		satur_code = 8
		for i in range(len(tvdss)):
			if zones[i] == zone:
				if satur[i] == satur_code and satur[i+1] == 2:
					#print(satur[i])
					owc_tvdss.append(round(tvdss[i],0))
			#print("owc_tvdss", ds, owc_tvdss)
		bot_oil_tvdss = []
		top_water_tvdss = []
		for i in range(len(tvdss)):
			if zones[i] == zone:
				if satur[i] == satur_code and satur[i+1] != satur_code:
					#print(satur[i])
					bot_oil_tvdss.append(round(tvdss[i],0))
				if satur[i] == 2 and satur[i-1] != 2:
					top_water_tvdss.append(round(tvdss[i],0))

		#print("bot_oil_tvdss", ds, bot_oil_tvdss)
		#print("top_water_tvdss", ds, top_water_tvdss)
	else:
		pass
	return [well, ds, zone, owc_tvdss, bot_oil_tvdss,top_water_tvdss]

s = ";"
broken_wells = []
#print("well",s,"dataset", s, "zone", s,"owc", s, "X", s, "Y")
print("well",s,"dataset", s, "zone", s,"owc", s,"bot_oil",  s,"top_water", s, "X", s, "Y")
for well in db.selectedWellList():
	if "R" in well.split("-")[1]:
		pass
	else:
		try:
			ds_bdntc = "RIGIS_bdntc"	
			ds_gm = "RIGIS_gm"								#менять датасет с РИГИС
			zonation = "ZONES"							#менять датасет с ЗОНАМИ
			zone = "БВ2-0-1_TOP_S"							#указать зону интереса
			#print("test_dbntc",(Heff(well, ds_bdntc)))
			#print("test_gm",(Heff(well, ds_gm)))
			
			zone_list = db.variableLoad(well, zonation, "ZONES")
			x_list = db.variableLoad(well, zonation, "X")
			y_list = db.variableLoad(well, zonation, "Y")
			x = []
			y = []
			for i in range(len(zone_list)):
				if zone_list[i] == zone:
					x.append(x_list[i])
					y.append(y_list[i])
			
			#print(well, Heff(well, ds_gm)[1], zone,  Heff(well, ds_gm)[3][0], x[0], y[0])
			print(well, Heff(well, ds_gm)[1], zone, Heff(well, ds_gm)[3][0], x[0], y[0])
		except:
			broken_wells.append(well)
#print("broken wells list", broken_wells)
