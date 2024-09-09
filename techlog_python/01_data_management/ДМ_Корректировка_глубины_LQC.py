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
__date__ = """2022-04-06"""
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
import TechlogDialogAdvanced as tda

def depth_corr(well, ds, td_new):																										#Функция для корректировки глубины 
	s = ';'																																			#за счет копирования датасета со срезом
	ds_new = ds + '_new'																													#по глубине
	ref_name = db.referenceName(well, ds)
	md = db.variableLoad(well, ds, ref_name)
	ind_new = []
	for i in range(len(md)):
		if int(md[i]) == td_new:
			ind_new = i
	md_new = md[:ind_new]
	db.datasetCreate(well, ds_new , ref_name, 'Measured Depth', 'm', md_new, 'double')
	for var in db.variableList(well, ds):
		db.variableCopy(well, ds, var, ds_new, var, 'automatic', 'project', 'project', -1, 0, 0)
	db.datasetDelete(well, ds)
	db.datasetRename(well, ds_new, ds)
	return print(well, s, ds, s, md[ind_new])

dlg = tda.dialogAdvanced("Глубина LQC & GBD")
dlg.addDoubleInput('td_new', 'Глубина новая', 0, 0, 5000, 0, 1, "help")
dlg.execDialog()
td_new = dlg.getDoubleInput('td_new')
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
		depth_corr(well, ds, td_new)
#for well in db.selectedWellList():
	#depth_corr(well, 'GDB_LOGS', td_new)
	#depth_corr(well, 'LQC', td_new)
	
