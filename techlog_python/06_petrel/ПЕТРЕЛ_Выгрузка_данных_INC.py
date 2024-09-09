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
inc_path = 'E:\\Petrel\\Exchange\\INC'
ds_inc = 'inclination'
inc_var_list = ['MD', 'AZI', 'INC', 'AZIM', 'INCL']																	#Выгрузка инклинометрии в формате лас
for well in db.selectedWellList():
	db.datasetCopy(well, ds_inc, 'project', 'export')
	db.currentChange('export')
	uwi_name = db.wellPropertyValue(well, 'UWI')
	new_well_name = uwi_name .split('_')[0] + '_' + well.split('-')[1]
	db.wellRename(well, new_well_name)
	for var in db.variableList(well, ds_inc):
		if var not in inc_var_list:
			db.variableDelete(well, ds_inc, var)
	db.exportFile(inc_path + '\\' + new_well_name + '.las', [new_well_name + '.' + ds_inc], 'LAS 2.0', 0, 0)
db.currentChange('project')

#path = os.path.realpath('E:\\Petrel\\Exchange\\INC\\')
#os.startfile('E:\\Petrel\\Exchange\\INC\\')
