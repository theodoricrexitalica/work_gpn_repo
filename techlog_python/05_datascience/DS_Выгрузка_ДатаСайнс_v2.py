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
__date__ = """2022-10-17"""
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
import csv
import os

def flatten(lst):
	for x in lst:
		if isinstance(x, list):
			yield from flatten(x)
		else:
			yield x

def copy_var(dsList, varList):
	for var in varList:
		if db.variableExists(well, dsList, var):
			db.variableCopy(well, dsList, var, dsDist, var, 'automatic')
		else:
			db.variableCreate(well, dsDist, var, 1)
	return
	
def dubl_dsdist(dsScr, dsDist):
	if db.datasetExists(well, dsScr):
		db.datasetDuplicate(well, dsScr, well, dsDist)
		for var in db.variableList(well, dsDist):
			if var != db.referenceName(well, dsDist):
				db.variableDelete(well, dsDist, var, 1)
	else:
		pass
		#print(dsScr, 'ds not exist')
	return

dsInd = 'Index'
dsLqc = 'LQC'
dsRigis = 'RIGIS_gm'
dsZone = 'ZONES_gm'
dsDist = 'TEMP'
varInd = ['TVDSS']
varLqc = ['GR', 'RT_DP', 'RT_SH','RT_ED', 'RT_MD', 'RHOB', 'W', 'RT', 'SP']
varRigis = ['rp','kng', 'kp', 'kvo', 'lit', 'kol', 'satur']
varZones = ['X', 'Y', 'ZONES']
dictList = {dsInd:varInd, dsRigis: varRigis, dsLqc:varLqc, dsZone:varZones}

varCount = 0
for i in dictList.keys():
	varCount += len(dictList[i])

for well in db.selectedWellList():
	if db.datasetExists(well, dsDist):
		pass
	else:
		dubl_dsdist(dsInd, dsDist)
		for ds in dictList:
			if db.datasetExists(well, ds):
				copy_var(ds, dictList[ds])
			else:
				for i in range(len(dictList[ds])):
					db.variableCreate(well, dsDist, dictList[ds][i], 1)
	db.datasetCopy(well, dsDist, 'project', 'export')
db.currentChange('export')
for well in db.wellList():
	db.wellRename(well, db.wellPropertyValue(well, 'Short_well_name'))
	
	#dataHeader = ['well_ngt', 'well']
	#for var in db.variableList(well, dsDist):
		#dataHeader.append(var)

#for well in db.selectedWellList()[:1]:
	#projName = (well.split('-')[0]).lower()
	#projName = projName + '_ds_techlog.csv'
#print(projName)
#path_e = 'E:\\Jupyter'
#dataPath = os.path.join(path_e, projName)

#with open(dataPath, 'w', encoding='UTF8', newline='') as f:
	#writer = csv.writer(f, delimiter=';')
	#writer.writerow(dataHeader)
	#for well in db.selectedWellList():
		#listData = []
		#for name in dataHeader[2:]:
			#listData.append(db.variableLoad(well, dsDist, name)[:])
		#well_ngt = db.wellPropertyValue(well, 'Short_well_name')
		#try:
			#for i in range(len(listData[0])):
				#lines = flatten([well_ngt, well.split('-')[1], [listData[j][i] for j in range(varCount+1)]])
				#writer.writerow(lines)
		#except:
			#print(well + ' no TEMP')
			#pass
#os.startfile(path_e)
#for well in db.selectedWellList():
	#dsDist = 'TEMP'
	#try:
		#db.datasetDelete(well, dsDist)
	#except:
		#pass
