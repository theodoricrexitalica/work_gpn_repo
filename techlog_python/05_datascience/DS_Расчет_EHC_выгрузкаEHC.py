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
__date__ = """2023-02-27"""
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
def ds_create(well):
	dsRigisGm = 'RIGIS_gm'
	dsZoneGm = 'ZONES_gm'
	if db.datasetExists(well, dsRigisGm) and db.datasetExists(well, dsZoneGm):
		db.datasetDuplicate(well, dsRigisGm, well, 'rigis_gm_temp')
		db.variableCopy(well, dsZoneGm, 'ZONES', 'rigis_gm_temp', 'ZONES', 'automatic', 'project', 'project', -1, 0, 1)
		db.variableCopy(well, dsZoneGm, 'X', 'rigis_gm_temp', 'X', 'automatic', 'project', 'project', -1, 0, 1)
		db.variableCopy(well, dsZoneGm, 'Y', 'rigis_gm_temp', 'Y', 'automatic', 'project', 'project', -1, 0, 1)

def ds_export(well):
	if db.datasetExists(well, 'rigis_gm_temp'):
		db.datasetCopy(well, 'rigis_gm_temp','project', 'export')
		db.datasetDelete(well, 'rigis_gm_temp',1)
	else:
		pass

for well in db.selectedWellList():
	ds_create(well)
	
for well in db.selectedWellList():
	ds_export(well)

db.currentChange('export')
for well in db.wellList():
	new_name = str(db.wellPropertyValue(well, 'Short_well_name'))
	db.wellRename(well, new_name)
