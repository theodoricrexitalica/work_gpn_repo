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

__author__ = """Taras DOLGUSHIN (dolgushin.tyu)"""
__date__ = """2021-12-20"""
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
from itertools import groupby
well_cc = 0
ds_cc = 0
oil_cc = 0
broken_cc = 0
broken_wells_list = []
broken_zone_list = []
allwells_zone_list = []

for well in db.wellList():
#for well in db.selectedWellList():																		#переключение на случай, если надо выборку скважин проверить
	well_cc += 1
	ds = "RIGIS_gm"
	ds_zone = "ZONES_vyng_gm"
	if db.datasetExists(well, ds) and db.datasetExists(well, ds_zone) and db.variableExists(well, ds_zone, "X"):		#проверка есть ли датасеты
		ds_cc +=1																																						#с РИГИС, зонамии и переменные координат
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		zones = db.variableLoad(well, ds_zone, "ZONES")
		x_coord = db.variableLoad(well, ds_zone, "X")
		y_coord = db.variableLoad(well, ds_zone, "Y")
		satur = db.variableLoad(well, ds, "satur")
		top_depth = []
		bot_depth = []
		zone_oil_list = []
		x_oil_list = []
		y_oil_list = []
		for i in range(len(zones)):
			#if "ЮВ1" not in zones[i] and "БВ8" not in zones[i]:																#указание в каких пластах не искать
			if "БВ6" in zones[i]:
				try:
					ind1 = db.datasetZoneIndice(well, ds, ds_zone, zones[i], "Zone Name",0)[0]				#поиск индектов каждой зоны
					ind2 = db.datasetZoneIndice(well, ds, ds_zone, zones[i], "Zone Name",0)[1]
					for j in range(len(satur))[ind1:ind2]:
						if satur[j] == 8:
							zone_oil_list.append(zones[i])
							x_oil_list.append(x_coord[i])
							y_oil_list.append(y_coord[i])
							#if satur[j] == 8 and satur[j-1] != 8:																#поиск глубин начала и конца нефтекодов
								#top_depth.append(md[j])
							#if satur[j] == 8 and satur[j+1] != 8:
								#bot_depth.append(md[j])
			#print(well, zones[i], top_depth, bot_depth)																	#печать глубин начала и конца нефтекода
				except:
					broken_zone_list.append(well + ";" + zones[i])
					broken_cc += 1
		clean_zone_oil_list =  [x for x, y in groupby(zone_oil_list)]												#чистка списка от повторяющихся зон для одной скважины
		clean_x_oil_list = [x for x, y in groupby(x_oil_list)]															#чистка списка от повторяющихся координат для одной скважины
		clean_y_oil_list = [x for x, y in groupby(y_oil_list)]
		if len(clean_zone_oil_list) > 0:
			oil_cc += 1
			#print(well, clean_zone_oil_list)																					#вывод номеров скважин со списком зон
			for i in range(len(clean_zone_oil_list)):																		#отображение скважин и зон в виде бегущего списка
				try:
					#allwells_zone_list.append(clean_zone_oil_list[i])													#добавление всех зон в глобальный список
					#print(well, clean_zone_oil_list[i])																			#вывод номеров скважин и зон построчно
					print(well, clean_zone_oil_list[i], clean_x_oil_list[i], clean_y_oil_list[i])				#вывод номеров скважин, зон и координат построчно
				except:
					broken_zone_list.append(well + ";" + zones[i])
					broken_cc += 1
	else:
		broken_wells_list.append(well)
print("well_cc", "ds_cc", "oil_cc", "broken_cc")
print(well_cc, ds_cc, oil_cc, broken_cc)
#print(broken_zone_list)
#print(broken_wells_list)


#clean_allwells_zone_list = []																									#подсчет количества нефтекодов в каждом 
#for i in allwells_zone_list:																										#стратиграфическом интервале
	#j = str(i) + ";" + str(allwells_zone_list.count(i))
	#clean_allwells_zone_list.append(j)
#final_list = set(clean_allwells_zone_list)
#for i in final_list:
	#print(i)
