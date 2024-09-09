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
__date__ = """2022-01-18"""
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
#from itertools import groupby

#ДОПИСАТЬ ПРОВЕРКА НАЛИЧИЯ ДАТАСЕТА PERF

for well in db.selectedWellList():
	ds = "PERF"
	if not db.datasetExists(well, ds):
		pass
	else:
		print(well)
		md = db.variableLoad(well, ds, db.referenceName(well, ds))
		top_perf = []
		bot_perf = []
		for i in range(len(md))[1::2]:
			bot_perf.append(round(md[i],1))
		for i in range(len(md))[0::2]:
			top_perf.append(round(md[i],1))
		print("tops_perfs, m", top_perf)
		print("bot_perf, m", bot_perf)
#for well in db.selectedWellList():
		if db.wellPropertyValue(well, "Status") == "Frac":
			print(well, "is fracked")
			pass
		else:
			md_bdntc = db.variableLoad(well, "RIGIS_bdntc", db.referenceName(well, "RIGIS_bdntc"))
			db.variableDuplicate(well, "RIGIS_bdntc", db.referenceName(well, "RIGIS_bdntc"), "PERF")
			db.variableFamilyChange(well, "RIGIS_bdntc", "PERF", "Perforation")
			perf = db.variableLoad(well, "RIGIS_bdntc", "PERF")
			for k in range(len(top_perf)):
				if md_bdntc[0] > top_perf[k]:
					top_perf[k] = md_bdntc[0]
			#print(top_perf)
			for i in range(len(perf)):
				perf[i] = -9999
			db.variableSave(well,  "RIGIS_bdntc", "PERF", "Perforation", "unitless", perf, 0, "double")
			ind1 = []
			ind2 = []
			for i in range(len(md_bdntc)):
				for j in range(len(top_perf)):
					if top_perf[j] == md_bdntc[i]:
						ind1.append(i)
					if bot_perf[j] == md_bdntc[i]:
						ind2.append(i)
			print("indice:", ind1, ind2)
			for k in range(len(ind1)):
				for q in range(len(md_bdntc))[ind1[k]:ind2[k]]:
					perf[q] = 1
			db.variableSave(well, "RIGIS_bdntc", "PERF", "Perforation", "unitless", perf, 0, "double")
			db.variableCopy(well, "RIGIS_bdntc", "PERF", "RIGIS_gm", "PERF", "zonation", "project", "project", -1, 0, 1)
