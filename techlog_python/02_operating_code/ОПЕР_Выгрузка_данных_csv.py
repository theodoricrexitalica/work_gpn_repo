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
__date__ = """2022-04-05"""
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

folder_path = 'E:\\Techlog_download\\'
file_name = 'Khol_well_date_drill.csv'																			#Имя файла для выгрузки рез-в
welldata_path = os.path.join(folder_path, file_name)
s = ';'
try:
	with open(welldata_path, 'r+') as file:																#Обнуление размера файла с данными для его очистки от предыдущей инфы
		file.truncate(0)
except:
	pass
for well in db.selectedWellList():
	ds = 'wellinfo'
	if (db.datasetExists(well, ds) 
	and db.variableLoad(well, ds, 'drilling_fin')[0] != MissingValue
	and db.variableLoad(well, ds, 'drilling_fin')[0] != ''):
		date = db.variableLoad(well, ds, 'drilling_fin')[0]
		coord_x = db.variableLoad(well, ds, 'x_td')[0]
		coord_y = db.variableLoad(well, ds, 'y_td')[0]

		print(well, s, coord_x, s, coord_y, s, date)													#Формирование строк для записи данных в файл
		lines = [well, s, str(coord_x), s, str(coord_y), s, str(date), "\n"]
		with open(welldata_path, 'a') as file:
			for line in lines:
				file.write(line)
	else:
		pass
	
