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
import TechlogDialogAdvanced as tda
import csv
import os

for well in db.selectedWellList():
	ds_zone = []
	for ds in db.datasetList(well):
		if 'ZONES' in ds:
			ds_zone.append(ds)
	dlg = tda.dialogAdvanced("Список датасетов")																				#Диалог для выбора датасета с зонами
	dlg.addListInput('ds_zones', 'Зонейшен датасет', ds_zone, 0, 0, '', [])
	dlg.execDialog()
	ds_zone_sel = dlg.getListInput('ds_zones')
	var_zone = db.variableLoad(well, ds_zone_sel, 'ZONES')
	
	dlg = tda.dialogAdvanced("Список зон")																						#Диалог для выбора целевой зоны
	dlg.addListInput('target_zone', 'Список зон', var_zone, 0, 0, '', [])
	dlg.addIntegerInput('well_quantity','Кол-во скважин', 5, 0, 100, 1)
	dlg.execDialog()
	target_zone = dlg.getListInput('target_zone')
	well_quantity = dlg.getIntegerInput('well_quantity')
	ds_zone = ds_zone_sel																						
	var_zone = target_zone																						
	break 

for well in db.selectedWellList():																											#Определение координат базовой скважины
	if db.datasetExists(well, ds_zone) and db.variableExists(well, ds_zone, 'ZONES'):
		ref_name = db.referenceName(well, ds_zone)
		ref = db.variableLoad(well, ds_zone, ref_name)
		zone_list = db.variableLoad(well, ds_zone, 'ZONES')
		target_zone_ind = []
		for i in range(len(ref)):
			if var_zone == zone_list[i]:
				target_zone_ind.append(i)
		if len(target_zone_ind) == 0:																										#Проверка есть целевой пласт в базовой скважине
			print(var_zone, 'is absent')
			quit()
		else:
			pass
		x_well = 'X'
		y_well = 'Y'
		coord_x_well = db.variableLoad(well, ds_zone, x_well)[target_zone_ind[0]]
		coord_y_well = db.variableLoad(well, ds_zone, y_well)[target_zone_ind[0]]
	else:
		print( ds_zone, 'is absent')
		quit()

distance = []
well_all_list = []
for well_all in db.wellList():																								#Расчет расстояния между базовой и всеми скважинами в проекте
	if db.datasetExists(well_all, ds_zone) and db.variableExists(well_all, ds_zone, 'ZONES'):
		ref_name = db.referenceName(well_all, ds_zone)
		ref = db.variableLoad(well_all, ds_zone, ref_name)
		zone_list = db.variableLoad(well_all, ds_zone, 'ZONES')
		target_zone_ind_all = []
		for i in range(len(ref)):
			if var_zone == zone_list[i]:
				target_zone_ind_all.append(i)
				x_all = 'X'
				y_all = 'Y'
				try:
					x_well = db.variableLoad(well_all, ds_zone, x_all)[target_zone_ind_all[0]]
					y_well = db.variableLoad(well_all, ds_zone, y_all)[target_zone_ind_all[0]]
					distance_well = round(sqrt((x_well - coord_x_well)**2 + (y_well - coord_y_well)**2), 0)
					distance.append(distance_well)
					well_all_list.append(well_all)
				except:
					pass
			else:
				pass
	else:
		pass

dict_distance = dict(zip(distance,well_all_list))																	#Создание словаря из списков скважин и расстояний
list_keys = list(dict_distance.keys())
list_keys.sort()																													#Сортировка ключей словаря

reportDir = db.dirTechlog()
csvFile = 'csvRep.csv'
path = os.path.join(reportDir, csvFile)																				#Формирование пути к файлу вывода списка скважин
with open(path, 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f, delimiter=';')
	writer.writerow(['well', 'distance'])
	for i in range(len(list_keys))[0:int(well_quantity)+1]:
		text = [dict_distance[list_keys[i]], list_keys[i]]
		print(dict_distance[list_keys[i]])
		writer.writerow(text)
os.startfile(path)
