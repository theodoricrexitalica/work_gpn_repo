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

__doc__ = """Создание списка скважин с сортировкой по дате"""
__author__ = """Taras DOLGUSHIN (dolgushin.tyu)"""
__date__ = """2022-04-01"""
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
import datetime as dt
well_cc = 0
prod_st_list = []
well_list = []
well_flaw = []
#for well in db.wellList():
for well in db.selectedWellList():
	well_cc += 1
	ds = 'wellinfo'
	var = 'production_start'																										#Можно указать какую переменную смотрим
	
	if (db.datasetExists(well, ds) 
		and db.variableLoad(well, ds, var)[0] != '' 
		and db.variableLoad(well, ds, var)[0] != -9999):															#Проверка наличия датасета, пустой строки или -9999
		
		well_list.append(well)
		prod_st = db.variableLoad(well, ds, var)[0]
		prod_st_list.append(dt.datetime.strptime(str(prod_st), '%d.%m.%y'))							#Иногда бывает длианная дата года, иногда короткая, надо менять %Y
	else:
		well_flaw.append(well)
dict_prod = dict(zip(prod_st_list, well_list))
keys_list = list(dict_prod.keys())																							#Создание списка ключей из словаря
keys_list.sort()																														#Сортировка списка ключей
cc = 0
for i in keys_list:
	if 'G' not in dict_prod[i]:
		cc += 1
		try:
			ds_zone = 'ZONES_gm'																							#Строка добавлена для уточнения зоны, до 
			zones_list = db.variableLoad(dict_prod[i], ds_zone, 'ZONES')
			print(str(i).split(' ')[0], dict_prod[i], zones_list[-1])
		except:
			pass
print('toral wells:', well_cc)
print('wells with data:', cc)
print('wells_flaw_list:', len(well_flaw))
