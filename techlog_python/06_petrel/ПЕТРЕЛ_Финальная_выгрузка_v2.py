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
__awiEngine__ = """v1"""
__layoutTemplateMode__ = """"""
__includeMissingValues__ = """True"""
__keepPreviouslyComputedValues__ = """True"""
__areInputDisplayed__ = """True"""
__useMultiWellLayout__ = """True"""
__idForHelp__ = """"""
__executionGranularity__ = """full"""
#DeclarationsEnd
import os 
import TechlogDialogAdvanced as tda

def folder_creation():
	path_upload_list = [	'E:\\Petrel\\Exchange\\',
									'Paste/type your own path...']
	dlg = tda.dialogAdvanced("Выгрузка Петрел")
	input = dlg.addListInput("path_upload_list", "Пусть выгрузки", path_upload_list, 0, 1, "help")
	dlg.execDialog()
	path_output = dlg.getListInput("path_upload_list")
	proj_folder_path = path_output
	list_path = ['inclination', 'las', 'rigis_gm', 'rigis_bdntc', 'tops', 'wellhead']
	folder_path = []
	try:
		os.mkdir(proj_folder_path)
	except:
		pass
	for folder_name in list_path:
		folder_path.append(os.path.join(proj_folder_path, folder_name))
		try:
			os.mkdir(os.path.join(proj_folder_path, folder_name))
			print(os.path.join(proj_folder_path, folder_name))
		except:
			pass
	return folder_path

def wellhead_download(path_wh):
	file_name = 'wellhead.txt'																					#Генерация пути для файла с велхедами
	file_path = os.path.join(path_wh, file_name)
	ds_wh = 'WH'
	with open(file_path, 'a') as file:
			file.truncate(0)
	for well in db.selectedWellList():																		#Копирование велхедов в текстовый файл
		if db.datasetExists(well, ds_wh):
			x = db.variableLoad(well, ds_wh, 'X-Coord')[0]
			y = db.variableLoad(well, ds_wh, 'Y-Coord')[0]
			kb =  db.variableLoad(well, ds_wh, 'KB')[0]	
			uwi_name = db.wellPropertyValue(well, 'UWI')
			new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1]
			lines = [new_well_name, '\t', str(x), '\t', str(y), '\t', str(kb), "\n"]
			with open(file_path, 'a', encoding = 'ansi') as file:
				for line in lines:
					file.write(line)
		else:
			pass
			print(well, ds_wh, ' is absent, check well')
	return

def inclination_download(path_inc):
	inc_var_list = ['MD', 'AZI', 'INC', 'AZIM', 'INCL']																	#Выгрузка инклинометрии в формате лас
	ds_inc = 'inclination'
	for well in db.selectedWellList():
		if db.datasetExists(well, ds_inc):
			db.datasetCopy(well, ds_inc, 'project', 'export')
			db.currentChange('export')
			for var in db.variableList(well, ds_inc):
				if var not in inc_var_list:
					db.variableDelete(well, ds_inc, var)
			uwi_name = db.wellPropertyValue(well, 'UWI')
			new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1]
			db.wellRename(well, new_well_name)
			db.exportFile(path_inc + '\\' + new_well_name + '.las', [new_well_name + '.' + ds_inc], 'LAS 2.0', 0, 0)
		else:
			pass
			print(well, ds_inc, ' is absent, check well')
		db.currentChange('project')
	return

def las_download(ds_lqc, lqc_var_list, path_las):
	if db.variableExists(well, ds_lqc, 'RT') or 'G' in well:
		pass
	else:
		if db.datasetExists(well, 'RIGIS_gm'):
			db.variableCopy(well, 'RIGIS_gm', 'rp', ds_lqc, 'RT_rigis', 'automatic', 'project', 'project', -1, 0, 1)
			db.variableFamilyChange(well, ds_lqc, 'RT_rigis', 'Formation Resistivity')
		else:
			db.variableCopy(well, 'RIGIS_bdntc', 'rp', ds_lqc, 'RT_rigis', 'automatic', 'project', 'project', -1, 0, 1)
			db.variableFamilyChange(well, ds_lqc, 'RT_rigis', 'Formation Resistivity')
	db.datasetCopy(well, ds_lqc, 'project', 'export')
	db.currentChange('export')
	for var in db.variableList(well, ds_lqc):
		if var not in lqc_var_list:
			db.variableDelete(well, ds_lqc, var)
	if  db.variableExists(well, ds_lqc, 'W'):
		db.variableDelete(well, ds_lqc, 'CFTC')
	uwi_name = db.wellPropertyValue(well, 'UWI')
	new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1] 
	db.wellRename(well, new_well_name)
	db.exportFile(path_las + '\\' + new_well_name + '.las', [new_well_name + '.' + ds_lqc], 'LAS 2.0', 0, 0)
	db.currentChange('project')
	return
	
def tops_download(file_name, ds_zone, path_tops):
	file_path = os.path.join(path_tops, file_name)																					
	with open(file_path, 'a') as file:
			file.truncate(0)
	for well in db.selectedWellList():																								#Копирование отбивок в текстовый файл
		if db.datasetExists(well, ds_zone):
			uwi_name = db.wellPropertyValue(well, 'UWI')
			new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1] 
			md = db.variableLoad(well, ds_zone, db.referenceName(well, ds_zone))
			zones = db.variableLoad(well, ds_zone, 'ZONES')
			for i in range(len(md)):
				with open(file_path, 'a', encoding='ansi') as file:
					file.write(new_well_name + '\t' + str(round(md[i],2)) + '\t' + str(zones[i]) + '\n')
		else:
			pass
			print(well, ds_zone, ' is absent, check well')
	return
	
def rigis_download(ds_rigis, path_rigis):
	if db.datasetExists(well, ds_rigis):
		db.datasetCopy(well, ds_rigis, 'project', 'export')
		db.currentChange('export')
		uwi_name = db.wellPropertyValue(well, 'UWI')
		new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1] 
		db.wellRename(well, new_well_name)
		db.exportFile(path_rigis + '\\' + new_well_name + '.las', [new_well_name + '.' + ds_rigis], 'LAS 2.0', 0, 0)
	else:
		print(well, ds_rigis, ' is absent, check well')
		pass
	db.currentChange('project')
	return 
	
path_list = folder_creation()
path_inc = path_list[0]
path_las = path_list[1]
path_rigis_gm = path_list[2]
path_rigis_bd = path_list[3]
path_tops = path_list[4]
path_wh = path_list[5]

for well in db.selectedWellList():
	ds_lqc = 'LQC'
	#lqc_var_list = ['MD', 'DEPT','GR' ]
	lqc_var_list = ['MD', 'DEPT','GR', 'RT', 'W', 'SP', 'RHOB', 'RT_rigis', 'CFTC', 'RT_DP', 'RT_SH' ]
	ds_rigis_gm = 'RIGIS_gm'
	ds_rigis_bd = 'RIGIS_bdntc'
	inclination_download(path_inc)
	las_download(ds_lqc, lqc_var_list, path_las)
	rigis_download(ds_rigis_gm, path_rigis_gm)
	rigis_download(ds_rigis_bd, path_rigis_bd)

ds_zone = 'ZONES_gm'
file_name = 'welltops_gm.txt'
print(path_tops)
tops_download(file_name, ds_zone, path_tops)
wellhead_download(path_wh)
ds_zone = 'ZONES_bdntc'
file_name = 'welltops_bdntc.txt'
tops_download(file_name,ds_zone, path_tops)

openFolderPath = path_list[0].split('\\')[:4]
os.startfile('\\'.join(openFolderPath))
