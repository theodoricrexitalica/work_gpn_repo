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
__date__ = """2022-02-22"""
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
import TechlogStat as ts
import statistics as stat
ds_zone = 'ZONES_ety_gm'																								#Указание датасета с зонами для ГС
ds_datascience = 'DATASCIENCE'
ds_datascience_name = 'DS_Ety_18_3m'																			#Название датасета для результатов
percent = 90
month = 3																															#Количество месяцев для округления обводненности
ref_name = []
well_id = []
zone_id = []
mode_tvdss = []
watercut = []
cc = 0
s = ";"
#print("well", s, "percent", s, "TVDSS", s, "WC", s, "zone")
#print("well", s, "zone", s, 'P10', s, "mode_TVDSS", s, "P90", s, "WC")
for well in db.selectedWellList():									#ПОМЕНЯТЬ ИМЕНА ПЕРЕМЕННЫХ И ДОПИСАТЬ РАСЧЕТ СР ДЕБИТА ПО НЕФТИ
	if "G" in well:
		ds_index = "Index"
		var = "TVDBML"
		zone_name = db.variableLoad(well, ds_zone, 'ZONES')[-1]									#Поиск названия последней зоны
		zone_indice = db.datasetZoneIndice(well, ds_index, ds_zone, zone_name, "Zone Name", 0)
		tvdbml = db.variableLoad(well, ds_index, var)
		ind1_tvdss = zone_indice[0]
		ind2_tvdss = zone_indice[1]
		hrz = tvdbml[ind1_tvdss:ind2_tvdss]																		#Указание диапазона согласно зонейшену для поиска моды по АО
		cc += 1
		watercut_value =db.variableLoad(well, "MER", "watercut")[0: month]					#Указание интервала для расчета обводненности
		watercut_avg = round(stat.mean(watercut_value),2)
		oil_value =db.variableLoad(well, "MER", "oil")[0: month]										#Указание интервала для расчета дебита нефти
		oil_avg = round(stat.mean(oil_value),2)
		func = lambda x: round(x,1)																					#Округление значений  глубины АО до 1 знака после запятой
		round_hrz = list(map(func, hrz))																				
		mode_hrz = stat.mode(round_hrz)
		#print(well, s, str(percent) + "%", s, round(ts.percentile(hrz, percent, 1),0), s, watercut_avg, s, zone_name)
		#print(well, s, zone_name, s, mode_hrz, s, watercut_avg)										#Вывод результатов
		print(well, s, zone_name, s, mode_hrz, s, oil_avg)
		#print(well, s, zone_name, s, round( ts.percentile(hrz, 10, 1), 1), s, mode_hrz, s, round(ts.percentile(hrz, 90, 1),1), s, watercut_avg)
		ref_name.append(cc)																								#Создание списков с результатами
		well_id.append(well)
		zone_id.append(zone_name)
		mode_tvdss.append(mode_hrz)
		watercut.append(watercut_avg)
	else:
		pass

#db.wellCreate(ds_datascience)																						#Создание скважины и запись в датасет и переменные результатов
#db.datasetCreate(ds_datascience, ds_datascience_name, 'Ref', 'Reference', 'unitless', ref_name, 'float')
#db.variableSave(ds_datascience, ds_datascience_name, 'well_id', '', '', well_id, 0, 'auto')
#db.variableSave(ds_datascience, ds_datascience_name, 'zone_id', '', '', zone_id, 0, 'auto')
#db.variableSave(ds_datascience, ds_datascience_name, 'mode_tvdss', '', '', mode_tvdss, 0, 'auto')
#db.variableSave(ds_datascience, ds_datascience_name, 'watercut', '', '', watercut, 0, 'auto')
