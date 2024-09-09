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
__date__ = """2022-11-25"""
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
import csv

def flatten(lst):
	for x in lst:
		if isinstance(x, list):
			yield from flatten(x)
		else:
			yield x

dsInd = 'Index'
dsLqc = 'LQC'
dsRigis = 'RIGIS_gm'
dsZone = 'ZONES_gm'
dsDist = 'TEMP'
varInd = ['TVDSS']
varLqc = ['GR', 'RT_DP', 'RT_SH', 'RHOB', 'W', 'RT', 'SP']
varRigis = ['rp','kng', 'kp', 'kvo', 'lit', 'satur']
varZones = ['X', 'Y', 'ZONES']
dictList = {dsInd:varInd, dsRigis: varRigis, dsLqc:varLqc, dsZone:varZones}

varCount = 0
for i in dictList.keys():
	varCount += len(dictList[i])
	
for well in db.selectedWellList():	
	dataHeader = ['wellName']
	for var in db.variableList(well, dsDist):
		dataHeader.append(var)

with open('E://data.csv', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(dataHeader)
	for well in db.selectedWellList():	
		listData = []
		for name in dataHeader[1:]:
			listData.append(db.variableLoad(well, dsDist, name)[:])
		for i in range(len(listData[0])):
			#lines = [well, 
						#listData[0][i], listData[1][i], listData[2][i], listData[3][i], 
						#listData[4][i], listData[5][i], listData[6][i], listData[7][i],
						#listData[8][i], listData[9][i],  listData[10][i],  listData[11][i],
						#listData[12][i], listData[13][i],  listData[14][i],  listData[15][i],
						#listData[16][i]]
			varCount
			lines = flatten([well, [listData[j][i] for j in range(varCount+1)]])
			writer.writerow(lines)
for well in db.selectedWellList():
	dsDist = 'TEMP'
	db.datasetDelete(well, dsDist)
	os.startfile('E:\\')
