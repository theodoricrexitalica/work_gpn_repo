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
__date__ = """2022-10-25"""
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
def H_calculation(well, ds = 'RIGIS_gm', var = 'lit', tvdss = 'TVDSS'): 
	litList = db.variableLoad(well, ds, var)
	mdList = db.variableLoad(well, ds, db.referenceName(well, ds))
	tvdssList = db.variableLoad(well, ds, tvdss)
	layMdList = []
	layTVDList = []
	for i in range(len(mdList)):
		if litList[i] == 1 and litList[i-1] != 1:
			layMdList.append(mdList[i])
			layTVDList.append(tvdssList[i])
		if litList[i] != 1 and litList[i-1] == 1:
			layMdList.append(mdList[i])
			layTVDList.append(tvdssList[i])
	db.datasetCreate(well, ds + '_lay', 'MD', 'Measured Depth', 'm', layMdList)
	db.datasetTypeChange(well, ds + '_lay', 'interval')
	Hmd = []
	Htvdss = []
	for j in range(len(layMdList)):
		if j == len(layMdList)-1:
			break
		else:
			hmd = round((layMdList[j+1] - layMdList[j]),2)
			htvdss = round((layTVDList[j+1] - layTVDList[j]),2)
		Hmd.append(hmd)
		Htvdss.append(htvdss)
	Hmd.append(-9999)
	Htvdss.append(-9999)
	db.variableSave(well, ds + '_lay', 'H', 'Thickness', 'm', Hmd)
	db.variableSave(well, ds + '_lay', 'H_TVD', 'Thickness', 'm', Htvdss)
	db.variableCopy(well, ds, 'lit', ds + '_lay', 'lit', 'automatic', 'project', 'project', -1, 0, 1)
	db.variableCopy(well, ds, 'satur', ds + '_lay', 'satur', 'automatic', 'project', 'project', -1, 0, 1)
	return

def tvdss_copy(well, ds = 'RIGIS_gm'):
	db.variableCopy(well, 'Index', 'TVDSS',ds, 'TVDSS', 'anti-aliasing', 'project', 'project', -1, 0, 1)
	tvdss_bot_ind = float(db.variableInformation(well, ds, 'TVDSS', 'BottomIndex'))
	ref_bot_ind = float(db.variableInformation(well, ds,db.referenceName(well, ds), 'BottomIndex'))
	if tvdss_bot_ind + 100 < ref_bot_ind:
		print( 'Problem with TVDSS lenght')
		print(well, ds, tvdss_bot_ind, ref_bot_ind)
	return 

for well in db.selectedWellList():
	if db.datasetExists(well, 'RIGIS_gm'):
		tvdss_copy(well, 'RIGIS_gm')
		H_calculation(well, 'RIGIS_gm')
	else:
		print('RIGIS_gm is absent')
		pass
	if db.datasetExists(well, 'RIGIS_bdntc'):
		tvdss_copy(well, 'RIGIS_bdntc')
		H_calculation(well, 'RIGIS_bdntc')
	else:
		print('RIGIS_bdntc is absent')
		pass
	if db.datasetExists(well, 'RIGIS_td'):
		tvdss_copy(well, 'RIGIS_td')
		H_calculation(well, 'RIGIS_td')
	else:
		pass
