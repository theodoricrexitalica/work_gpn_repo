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
wellhead_path = 'E:\\Petrel\\Exchange\\WH\\wellheads.txt'
ds_wh = 'WH'
with open(wellhead_path, 'a') as file:
		file.truncate(0)
for well in db.selectedWellList():																								#Копирование велхедов в текстовый файл
	x = db.variableLoad(well, ds_wh, 'X-Coord')[0]
	y = db.variableLoad(well, ds_wh, 'Y-Coord')[0]
	kb =  db.variableLoad(well, ds_wh, 'KB')[0]	
	uwi_name = db.wellPropertyValue(well, 'UWI')
	new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1]
	lines = [new_well_name, '\t', str(x), '\t', str(y), '\t', str(kb), "\n"]
	with open(wellhead_path, 'a', encoding = 'ansi') as file:
		for line in lines:
			file.write(line)

#path = os.path.realpath('E:\\Petrel\\Exchange\\WH\\')
#os.startfile('E:\\Petrel\\Exchange\\WH\\')
