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

__doc__ = """Имена колонок в csv-файле
UWI ДАТА_ПЕРЕХОДА СТАТУС_СКВАЖИНЫ СИТУАЦИЯ_НА_СКВАЖИНЕ

"""
__author__ = """Taras DOLGUSHIN (dolgushin.tyu)"""
__date__ = """2022-03-23"""
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

format_data = '%d.%m.%y %H:%M:%S'

def split_time(var):
	result = var.split(" ")[0]
	return result

tempFile = rtc.getOpenFileName("Well Tops", multiselect = True, filter = ["All files;*.*"])
well_uwi = [] 
data = []
s = ';'
ds_name = 'wellstatus'
db.currentChange("import")
with open(tempFile[0], "r", -1, "ansi") as file:
	for line in file.readlines()[1:]:
		line = line.replace("\n", "")
		well_uwi.append(line.split(";")[1])															#Находим колонку с именем скважин в соответствующей позиции csv-файла
		data.append(line.split(";")[3:])																#Указываем номер позиции csv-файла, с которой начинаем отсчет колонок с данными

for i in range(len(well_uwi))[:10]:
	db.wellCreate(well_uwi[i])
for well in db.wellList():
	date_change = []
	well_status = []
	for i in range(len(well_uwi)):
		if well == well_uwi[i]:
			time = (datetime.datetime.strptime(data[i][0], format_data)).strftime( '%d.%m.%Y')
			date_change.append(time)
			well_status.append(data[i][1])
	db.datasetCreate(well, ds_name, "Ref", "Reference", "m", [1], "float")
	db.datasetTypeChange(well, ds_name, "point data")
	db.variableSave(well, ds_name, "date", " ", "", date_change, 0, "string")
	db.variableTypeChange(well, ds_name, "date", 'Continu')
	db.variableSave(well, ds_name, "well_status", " ", "", well_status, 0, "string")
	db.variableTypeChange(well, ds_name, "well_status", 'Continu')
