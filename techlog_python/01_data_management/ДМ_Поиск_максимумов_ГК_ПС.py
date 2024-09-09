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

__author__ = """Taras DOLGUSHIN (Dolgushin.TYu)"""
__date__ = """2021-07-07"""
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
import TechlogStat as ts

list_gr = []
list_md = []
for well in db.selectedWellList():
	ds = "GDB_LOGS"
	for var in db.variableList(well, ds):
		if "GR" in var:
			gr = db.variableLoad(well, ds, var)
			md = db.variableLoad(well, ds, db.referenceName(well, ds))
			for i in range(len(gr)):
				if gr[i] >0 and gr[i+1] == -9999:
					list_gr.append(var)
					list_md.append(md[i])
index = list_md.index(max(list_md))
print(well.split("-")[1], list_gr[index], round(max(list_md),0))
gr_orig_name = list_gr[index]
db.variableRename(well, ds, gr_orig_name, "GR")

list_sp = []
list_md = []
for well in db.selectedWellList():
	ds = "GDB_LOGS"
	for var in db.variableList(well, ds):
		if "SP" in var:
			gr = db.variableLoad(well, ds, var)
			md = db.variableLoad(well, ds, db.referenceName(well, ds))
			for i in range(len(gr)):
				if gr[i] >0 and gr[i+1] == -9999:
					list_sp.append(var)
					list_md.append(md[i])
index = list_md.index(max(list_md))
print(well.split("-")[1], list_sp[index], round(max(list_md),0))
sp_orig_name = list_sp[index]
db.variableRename(well, ds, sp_orig_name, "SP")
