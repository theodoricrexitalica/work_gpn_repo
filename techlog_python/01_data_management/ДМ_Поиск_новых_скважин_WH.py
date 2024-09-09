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

db.currentChange("project")
current_wells = db.wellList()
for well in db.selectedWellList():
	uwi = db.wellPropertyValue(well, "Field")
current_wells_cleaned = list(map(lambda x: x.split("-")[1],current_wells))
db.currentChange("import")

#tempFolder = "E:\\OilFields\\Вынгапуровское\\КП_436_427_БВ5\\zones\\"
#tempFile = os.path.join(tempFolder , "Well_Header")
tempFile = rtc.getOpenFileName("Well Tops", multiselect = True, filter = ["All files;*.*"])

wells_txt = [] 
with open(tempFile[0], "r", -1, "ansi") as file:
	for line in file.readlines()[1:]:
		line = line.replace("\n", "")
		well_name = line.split(" ")[0]
		wells_txt.append(well_name)

new_well = map(lambda x: x.split("_")[1], wells_txt)
list_difference = []
for well in new_well:
	if well not in current_wells_cleaned:
		list_difference.append(well)
for i in list_difference:
	if "S" in i:
		pass
	else:
		print(uwi + "_" + i + ",")
	
