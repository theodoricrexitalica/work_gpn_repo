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
#wellhead_path = 'E:\\Petrel\\Exchange\\WH\\wellheads.txt'
#ds_wh = 'WH'
#for well in db.selectedWellList():																								#Копирование велхедов в текстовый файл
	##kb =  db.variableLoad(well, ds_wh, 'KB')[0]						
	##x = db.variableLoad(well, ds_wh, 'X-Coord')[0]
	##y = db.variableLoad(well, ds_wh, 'Y-Coord')[0]
	##lines = [well, '\t', str(x), '\t', str(y), '\t', str(kb), "\n"]
	##with open(wellhead_path, 'a') as file:
		##for line in lines:
			##file.write(line)

#inc_path = 'E:\\Petrel\\Exchange\\INC'
#ds_inc = 'inclination'
#inc_var_list = ['MD', 'AZI', 'INC', 'AZIM', 'INCL']																	#Выгрузка инклинометрии в формате лас
#for well in db.selectedWellList():												
	#db.datasetCopy(well, ds_inc, 'project', 'export')
	#db.currentChange('export')
	#for var in db.variableList(well, ds_inc):
		#if var not in inc_var_list:
			#db.variableDelete(well, ds_inc, var)
	#db.exportFile(inc_path + '\\' + well + '.las', [well + '.' + ds_inc], 'LAS 2.0', 0, 0)
#db.currentChange('project')

def gr_index(well, ds, var):																										#Функция поиска последнего значения не равного -9999
	gr = db.variableLoad(well, ds, var)
	gr_ind = []
	for i in range(len(gr)):
		if gr[i] != -9999 and gr[i+1] == -9999:
			gr_ind.append(i)
	return gr_ind[0]

target_zone = ["БС12_TOP_S"]
for well in db.selectedWellList():
	ds_gr = 'LQC'
	ds_zone = 'ZONES_kar_gm'
	ind = db.datasetZoneIndice(well, ds_gr, ds_zone, target_zone[0], 'Zone Name', 1)
	ds_gbd = 'GDB_LOGS'
	var_list = []
	ind_list = []
	for var in db.variableList(well, ds_gbd):
		if db.variableFamily(well, ds_gbd, var) == 'Russian Gamma Ray':
			#print(var, gr_index(well, ds_gbd, var))
			var_list.append(var)
			ind_list.append(gr_index(well, ds_gbd, var))
	max_ind = ind_list.index(max(ind_list))																					#Поиск максимального индекса 
	target_var = var_list[max_ind]																									#Имя переменной с макс индексом
	#print(target_var)
	new_name_target_var = target_var.split("_")[0]
	db.variableRename(well, ds_gbd, target_var, new_name_target_var)
	db.variableCopy(well, ds_gbd, new_name_target_var, ds_gr, new_name_target_var, 'automatic', 'project', 'project', -1, 0, 1)
	db.variableRename(well, ds_gbd, new_name_target_var, target_var)
	
	lqc_path = 'E:\\Petrel\\Exchange\\LAS'
	db.datasetCopy(well, ds_gr, 'project', 'export')
	db.currentChange('export')
	lqc_var_list = [db.referenceName(well, ds_gr), new_name_target_var]
	for var in db.variableList(well, ds_gr):
		if var not in lqc_var_list:
			db.variableDelete(well, ds_gr, var)
	db.exportFile(lqc_path + '\\' + well + '.las', [well + '.' + ds_gr], 'LAS 2.0', 0, 0)
db.currentChange('project')
