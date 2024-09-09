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
__date__ = """2022-04-20"""
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

def var_top_bot(var):																								#Функция для поиска максимумов и минимумов в каротаже
	top_var = []
	bot_var = []
	for i in range(len(var)):
		if var[i] != MissingValue and var[i-1] == MissingValue:
			top_var.append(i)
		elif var[i] != MissingValue and var[i+1] == MissingValue:
			bot_var.append(i)
	return [top_var[0], bot_var[0]]

def zones_indice(well, target_zone, ds_zones):														#Функция для поиска индексов целевого зонейшена
	ds_gbd = 'GDB_LOGS'
	zones_name_list = []
	zones_list = db.variableLoad(well, ds_zones, 'ZONES')
	gbd_md = db.variableLoad(well, ds_gbd, db.referenceName(well, ds_gbd))
	for zone_name in zones_list:																				#Поиск зонейшена в списке по маске
		if target_zone in zone_name:
			zones_name_list.append(zone_name)
	gbd_indice_top = []
	gbd_indice_bot = []
	for zones_ind in zones_name_list:
		gbd_indice = db.datasetZoneIndice(well, ds_gbd, ds_zones, zones_ind, 'Zone Name')
		gbd_indice_top.append(gbd_indice[0])															#Создание списков с минимума и максимума зонейшенов
		gbd_indice_bot.append(gbd_indice[1])
	min_ind = min(gbd_indice_top)																			#Поиск наивысшего индекса целевого зонейшена по маске
	max_ind = max(gbd_indice_bot)																			#Поиск низшего индекса целевого зонейшена по маске
	return  [min_ind, max_ind]

def copy_vars_lqc(well, min_ind, max_ind, var_family, delta):
	ds_gbd = 'GDB_LOGS'
	ds_lqc = 'LQC'
	list_depth = []
	list_var = []
	for var in db.variableList(well, ds_gbd):
		if var != db.referenceName(well, ds_gbd) and db.variableFamily(well, ds_gbd, var) == var_family:
			var_top = float(db.variableInformation(well, ds_gbd, var, 'TopIndex'))
			var_bot = float(db.variableInformation(well, ds_gbd, var, 'BottomIndex'))
			#print(var, min_ind, var_top, '-', var_bot, max_ind - delta)
			if var_top < min_ind and var_bot > max_ind + delta*10:								#Условие поиска индекса переменной выше и ниже индексов зонейшена
				#print(var, min_ind, var_top, '-', var_bot, max_ind, 'selected')
				list_depth.append(var_bot)
				list_var.append(var)
	dict_one = dict(zip(list_depth, list_var))																#Создание словаря с ключом глубины
	max_bot_var = max(dict_one.keys())																	#Поиск максимального ключа глубины
	name_max_bot_var =dict_one[max_bot_var]
	db.variableCopy(well, ds_gbd, name_max_bot_var, ds_lqc, name_max_bot_var.split('_')[0], 'automatic', 'project', 'project', -1, 0, 1)

var_family_list = ([
							'Russian Gamma Ray',
							'Spontaneous Potential',
							'Neutron Far',
							'Neutron Porosity',
							'Bulk Density',
							'Micro Gradient Resistivity',
							'Micro Potential Resistivity',
							'Formation Resistivity',
							'Resistivity 05',
							'Resistivity 07',
							'Resistivity 10',
							'Resistivity 14',
							'Resistivity 20',
							'Gradient 105',
							'Gradient 225',
							'Gradient 425',
							'Gradient 850',
							])
							
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
	dlg.addIntegerInput('delta','Дельта зоны', 0, -500, 500, 1)
	dlg.execDialog()
	target_zone = dlg.getListInput('target_zone')
	delta = dlg.getIntegerInput('delta')
	ds_gbd = 'GDB_LOGS'
	ds_lqc = 'LQC'
	try:
		min_ind = zones_indice(well, target_zone, ds_zone_sel)[0]
		max_ind = zones_indice(well, target_zone, ds_zone_sel)[1]
	except:
		print('Target zone is absent at well', well)
		break
	for var_family in var_family_list:
		try:
			copy_vars_lqc(well, min_ind, max_ind, var_family, delta)
		except:
			print(well, var_family, 'check the log in GBD_LOG')
			pass

	for var in db.variableList(well, ds_lqc):																					#Блок переименования скопированных переменных
		if 'Russian Gamma Ray' in db.variableFamily(well, ds_lqc, var):
			db.variableUnitChange(well,  ds_lqc, var, 'uR/h')
		if 'Spontaneous Potential' in db.variableFamily(well, ds_lqc, var):
			db.variableUnitChange(well,  ds_lqc, var, 'mV')
		if 'Neutron Far' in db.variableFamily(well, ds_lqc, var):
			db.variableUnitChange(well,  ds_lqc, var, 'UE')
		if 'Neutron Porosity' in db.variableFamily(well, ds_lqc, var):
			db.variableUnitChange(well,  ds_lqc, var, '%')
		if 'Bulk Density' in db.variableFamily(well, ds_lqc, var):
			db.variableUnitChange(well,  ds_lqc, var, 'g/cm3')
		if 'Resistivity' in db.variableFamily(well, ds_lqc, var):
			db.variableUnitChange(well,  ds_lqc, var, 'ohmm')
		if 'Gradient' in db.variableFamily(well, ds_lqc, var):
			db.variableUnitChange(well,  ds_lqc, var, 'ohmm')
