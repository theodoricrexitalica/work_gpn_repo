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
__date__ = """2022-06-14"""
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
import os 

def folder_creation():																						#Функция для создания папки проекта с подпапками
	proj_title = db.projectName()
	proj_folder_path = 'E:\\Petrel\\Exchange\\{}'.format(proj_title)
	list_path = ['wellhead', 'inclination', 'las', 'tops', 'rigis']
	for folder_name in list_path:
		try:
			os.mkdir(proj_folder_path + '\\' + folder_name)
		except:
			pass
	return proj_folder_path, list_path

#file_name = 'wellhead.txt'																					#Генерация пути для файла с велхедами
#folder_path = folder_creation()[0] + '\\' + folder_creation()[1][0]
#file_path = os.path.join(folder_path, file_name)
#with open(file_path, 'a') as file:
		#file.truncate(0)
#for well in db.selectedWellList():																		#Копирование велхедов в текстовый файл
	#ds_wh = 'WH'
	#if db.datasetExists(well, ds_wh):
		#x = db.variableLoad(well, ds_wh, 'X-Coord')[0]
		#y = db.variableLoad(well, ds_wh, 'Y-Coord')[0]
		#kb =  db.variableLoad(well, ds_wh, 'KB')[0]	
		#uwi_name = db.wellPropertyValue(well, 'UWI')
		#new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1]
		#lines = [new_well_name, '\t', str(x), '\t', str(y), '\t', str(kb), "\n"]
		#with open(file_path, 'a', encoding = 'ansi') as file:
			#for line in lines:
				#file.write(line)
	#else:
		#pass
		#print(well, ds_wh, ' is absent, check well')


#folder_path = folder_creation()[0] + '\\' + folder_creation()[1][1]
#inc_var_list = ['MD', 'AZI', 'INC', 'AZIM', 'INCL']																	#Выгрузка инклинометрии в формате лас
#for well in db.selectedWellList():
	#ds_inc = 'inclination'
	#if db.datasetExists(well, ds_inc):
		#db.datasetCopy(well, ds_inc, 'project', 'export')
		#db.currentChange('export')
		#for var in db.variableList(well, ds_inc):
			#if var not in inc_var_list:
				#db.variableDelete(well, ds_inc, var)
		#uwi_name = db.wellPropertyValue(well, 'UWI')
		#new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1]
		#db.wellRename(well, new_well_name)
		#db.exportFile(folder_path + '\\' + new_well_name + '.las', [new_well_name + '.' + ds_inc], 'LAS 2.0', 0, 0)
	#else:
		#pass
		#print(well, ds_inc, ' is absent, check well')
	#db.currentChange('project')


#folder_path = folder_creation()[0] + '\\' + folder_creation()[1][2]
#for well in db.selectedWellList():
	#ds_lqc = 'LQC'
	#if not db.variableExists(well, ds_lqc, 'RT'):
		#db.variableCopy(well, 'RIGIS_gm', 'rp', ds_lqc, 'RT_rigis', 'automatic', 'project', 'project', -1, 0, 1)
		#db.variableFamilyChange(well, ds_lqc, 'RT_rigis', 'Formation Resistivity')
	
	#db.datasetCopy(well, ds_lqc, 'project', 'export')
	#db.currentChange('export')
	
	#lqc_var_list = ['MD','GR', 'RT', 'W', 'SP', 'RHOB', 'RT_rigis', 'CFTC']
	#for var in db.variableList(well, ds_lqc):
		#if var not in lqc_var_list:
			#db.variableDelete(well, ds_lqc, var)
	#if  db.variableExists(well, ds_lqc, 'W'):
		#db.variableDelete(well, ds_lqc, 'CFTC')
	
	#uwi_name = db.wellPropertyValue(well, 'UWI')
	#new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1] 
	#db.wellRename(well, new_well_name)
	
	#db.exportFile(folder_path + '\\' + new_well_name + '.las', [new_well_name + '.' + ds_lqc], 'LAS 2.0', 0, 0)
	#db.currentChange('project')


#file_name = 'welltops.txt'																					
#folder_path = folder_creation()[0] + '\\' + folder_creation()[1][3]
#file_path = os.path.join(folder_path, file_name)
#with open(file_path, 'a') as file:
		#file.truncate(0)
#for well in db.selectedWellList():																								#Копирование отбивок в текстовый файл
	#ds_zone = 'ZONES_gm'
	#if db.datasetExists(well, ds_zone):
		#uwi_name = db.wellPropertyValue(well, 'UWI')
		#new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1] 
		#md = db.variableLoad(well, ds_zone, db.referenceName(well, ds_zone))
		#zones = db.variableLoad(well, ds_zone, 'ZONES')
		#for i in range(len(md)):
			#with open(file_path, 'a', encoding='ansi') as file:
				#file.write(new_well_name + '\t' + str(round(md[i],2)) + '\t' + str(zones[i]) + '\n')
	#else:
		#pass
		#print(well, ds_zone, ' is absent, check well')

folder_path = folder_creation()[0] + '\\' + folder_creation()[1][4]
for well in db.selectedWellList():
	ds_rigis = 'RIGIS_gm'
	if db.datasetExists(well, ds_rigis):
		db.datasetCopy(well, ds_rigis, 'project', 'export')
		db.currentChange('export')
		uwi_name = db.wellPropertyValue(well, 'UWI')
		new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1] 
		db.wellRename(well, new_well_name)
		db.exportFile(folder_path + '\\' + new_well_name + '.las', [new_well_name + '.' + ds_rigis], 'LAS 2.0', 0, 0)
	else:
		pass
		print(well, ds_rigis, ' is absent, check well')
	db.currentChange('project')

os.startfile(folder_creation()[0])
