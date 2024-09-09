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
lqc_path = 'E:\\Petrel\\Exchange\\LAS'
for well in db.selectedWellList():
	ds_lqc = 'LQC'
	if not db.variableExists(well, ds_lqc, 'RT'):
		db.variableCopy(well, 'RIGIS_gm', 'rp', ds_lqc, 'RT_rigis', 'automatic', 'project', 'project', -1, 0, 1)
		db.variableFamilyChange(well, ds_lqc, 'RT_rigis', 'Formation Resistivity')
	
	db.datasetCopy(well, ds_lqc, 'project', 'export')
	db.currentChange('export')
	
	lqc_var_list = ['MD','GR', 'RT', 'W', 'SP', 'RHOB', 'RT_rigis', 'CFTC']
	for var in db.variableList(well, ds_lqc):
		if var not in lqc_var_list:
			db.variableDelete(well, ds_lqc, var)
	if  db.variableExists(well, ds_lqc, 'W'):
		db.variableDelete(well, ds_lqc, 'CFTC')
	
	uwi_name = db.wellPropertyValue(well, 'UWI')
	new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1] 
	db.wellRename(well, new_well_name)
	
	db.exportFile(lqc_path + '\\' + new_well_name + '.las', [new_well_name + '.' + ds_lqc], 'LAS 2.0', 0, 0)
	db.currentChange('project')
	
path = os.path.realpath('E:\\Petrel\\Exchange\\LAS\\')
os.startfile('E:\\Petrel\\Exchange\\LAS\\')
