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
__date__ = """2022-03-10"""
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
def gr_index(well, ds, var):																								#Функция поиска последнего значения не равного -9999
	gr = db.variableLoad(well, ds, var)
	gr_ind = []
	for i in range(len(gr)):
		if gr[i] != -9999 and gr[i-1] == -9999:
			gr_ind.append(i)
		if gr[i] != -9999 and gr[i+1] == -9999:
			gr_ind.append(i)
	return gr_ind

target_zone = ["БП16_TOP_S"]																				#Не забыть указать нужный интервал
for well in db.selectedWellList():
	#print(well)
	ds_gbd = 'GDB_LOGS'
	ds_lqc = 'LQC'
	ds_zone = 'ZONES_ety_gm'
	ind_zone = db.datasetZoneIndice(well, ds_gbd, ds_zone, target_zone[0], 'Zone Name', 1)
	var_list = []
	for var in db.variableList(well, ds_gbd):
		if db.variableFamily(well, ds_gbd, var) == 'Russian Gamma Ray':
			gr_ind_values = gr_index(well, ds_gbd, var)													#Применение функции для поиска нужной переменной
			#print(well, var, ind_zone, gr_ind_values)
			if ind_zone == None:
				print(well, 'ind_zone is None')
				quit()
			elif gr_ind_values[0] < ind_zone[0] and gr_ind_values[1] > ind_zone[1]:			#Проверка закрывает ли переменная нужный интервал по глубине
				var_list.append(var)
			
	target_var = var_list[0]																								#Имя переменной которая соответствует условию проверки
	print(well, target_var)
	new_name_target_var = target_var.split("_")[0]														#Блок переименования и копирования выбранной переменной
	db.variableRename(well, ds_gbd, target_var, new_name_target_var)
	db.variableCopy(well, ds_gbd, new_name_target_var, ds_lqc, new_name_target_var, 'automatic', 'project', 'project', -1, 0, 1)
	db.variableRename(well, ds_gbd, new_name_target_var, target_var)
	
	lqc_path = 'E:\\Petrel\\Exchange\\LAS'																	#Блок экспорта ГК в виде лас-файла
	db.datasetCopy(well, ds_lqc, 'project', 'export')
	db.currentChange('export')
	lqc_var_list = [db.referenceName(well, ds_lqc), new_name_target_var]
	for var in db.variableList(well, ds_lqc):
		if var not in lqc_var_list:
			db.variableDelete(well, ds_lqc, var)
	db.exportFile(lqc_path + '\\' + well + '.las', [well + '.' + ds_lqc], 'LAS 2.0', 0, 0)
	db.currentChange('project')
