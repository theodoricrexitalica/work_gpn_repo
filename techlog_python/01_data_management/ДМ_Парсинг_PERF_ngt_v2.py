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

__doc__ = """Грузится файл с перфорациями из НГТ. Перфорации из НГТ надо сохранить как csv и ничего не редактировать в файле."""
__author__ = """Taras DOLGUSHIN (dolgushin.tyu)"""
__date__ = """2021-11-21"""
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
import RussianTools.RussianTools_Common as rtc
import os
import datetime
import TechlogDialogAdvanced as tda
from itertools import groupby

db.currentChange("import")
tempFile = rtc.getOpenFileName("Well Tops", multiselect = True, filter = ["All files;*.*"])

wells_txt = [] 
data_txt = []
with open(tempFile[0], "r", -1, "ansi") as file:																		#Открытие файла с перфорациями NGT
	for line in file.readlines()[1:]:
		line = line.replace("\n", "")
		well_name = line.split(";")[0]																						#Чтение имен скважин в нотации NGT
		wells_txt.append(well_name)
		data = line.split(";")[1:]																									#Чтение данныз по перфорации в виде списка строк
		data_txt.append(data)

current_date = datetime.datetime.now()
ds_perf = 'PERF_' + (current_date.strftime("%b%y"))								#Формирование имени датасета с МЭРами согласно текущему месяцу загрузки

db.currentChange("import")
for i in range(len(wells_txt)):
	db.wellCreate(wells_txt[i])
for well in db.wellList():
	list_md = []
	list_date = []
	list_zone = []
	list_type_perf = []
	list_type_tool = []
	list_perf_holes = []
	list_status = []
	list_perf = []
	for i in range(len(wells_txt)):
		if well == wells_txt[i]:
			try:
				list_md.append(float(data_txt[i][6]))																		#Создание списков с данными по колонкам из файла перфораций NGT
				list_md.append(float(data_txt[i][7]))
				list_date.append(data_txt[i][0])
				list_date.append(-9999)
				list_zone.append(data_txt[i][1])
				list_zone.append(-9999)
				list_type_perf.append(data_txt[i][3])
				list_type_perf.append(-9999)
				list_type_tool.append(data_txt[i][4])
				list_type_tool.append(-9999)
				list_perf_holes.append(data_txt[i][5])
				list_perf_holes.append(-9999)
				list_status.append(data_txt[i][13])
				list_status.append(-9999)
				list_perf.append(1)
				list_perf.append(-9999)
			except:
				pass
	db.datasetCreate(well, ds_perf, "MD", "Measured Depth", "m", list_md, "double")
	db.datasetTypeChange(well, ds_perf, "interval")
	db.variableSave(well, ds_perf, "Date", "Date", "unitless", list_date, 0, "auto")
	db.variableTypeChange(well, ds_perf, "Date", "RichText")
	db.variableSave(well, ds_perf, "Zones", "Zone Name", "unitless", list_zone, 0, "auto")
	db.variableTypeChange(well, ds_perf, "Zones", "RichText")
	db.variableSave(well, ds_perf, "Type_perf", "", "", list_type_perf, 0, "auto")
	db.variableTypeChange(well, ds_perf, "Type_perf", "RichText")
	db.variableSave(well, ds_perf, "Type_tool", "", "", list_type_tool, 0, "auto")
	db.variableTypeChange(well, ds_perf, "Type_tool", "RichText")
	db.variableSave(well, ds_perf, "Perf_holes", "", "", list_perf_holes, 0, "auto")
	db.variableTypeChange(well, ds_perf, "Perf_holes", "RichText")
	db.variableSave(well, ds_perf, "Status", "", "", list_status, 0, "auto")
	db.variableTypeChange(well, ds_perf, "Status", "RichText")
	db.variableSave(well, ds_perf, "PERF", "Perforation", "unitless", list_perf, 0, "double")

db.currentChange('project')
well_name = []
ngt_name = []
for well in db.wellList():																							#Чтение имени NGT в датасете скважины и формирование списков
	ds_wi = 'wellinfo'
	var_wi = 'well_ngt'
	if db.datasetExists(well, ds_wi):
		ngt_name_var= db.variableLoad(well, ds_wi, var_wi)
		well_name.append(well)
		ngt_name.append(ngt_name_var[0])
dict_wells = dict(zip(ngt_name, well_name))															#Создание словаря из 2х списков

db.currentChange('import')
for well_imported in db.wellList():
	for well_ngt in dict_wells:																						#Поиск совпадения ключей словаря со названиями скважин в импорте
		if well_ngt == well_imported:
			db.wellRename(well_ngt, dict_wells[well_ngt])
			print(well_ngt, dict_wells[well_ngt])
