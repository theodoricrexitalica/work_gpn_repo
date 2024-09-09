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
__date__ = """2022-03-21"""
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
ds_wellinfo = 'wellinfo'																										#Указываем датасет с координатами
well_quantity = 10

for well in db.selectedWellList():																						#Определение координат базовой скважины
	if db.datasetExists(well, ds_wellinfo):
		coord_x_well = db.variableLoad(well, ds_wellinfo, 'x_td')[0]
		coord_y_well = db.variableLoad(well, ds_wellinfo, 'y_td')[0]
	else:
		print( ds_wellinfo, 'is absent')
		quit()

distance = []
well_all_list = []
well_ngt_list = []
for well_all in db.wellList():																								#Расчет расстояния между базовой и всеми скважинами в проекте
	if db.datasetExists(well_all, ds_wellinfo):
		x_well = db.variableLoad(well_all, ds_wellinfo, 'x_td')[0]
		y_well = db.variableLoad(well_all, ds_wellinfo, 'y_td')[0]
		well_ngt = db.variableLoad(well_all, ds_wellinfo, 'well_ngt')[0]
		distance_well = round(sqrt((x_well - coord_x_well)**2 + (y_well - coord_y_well)**2), 0)
		distance.append(distance_well)
		well_all_list.append(well_all)
	else:
		pass

dict_distance = dict(zip(distance,well_all_list))																	#Создание словаря из списков скважин и расстояний
list_keys = list(dict_distance.keys())
list_keys.sort()																													#Сортировка ключей словаря
for i in range(len(list_keys))[0:well_quantity+1]:
	print('{0} : {1:.0f} m'.format(dict_distance[list_keys[i]], list_keys[i]))
