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
__date__ = """2022-10-20"""
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
dlg = tda.dialogAdvanced("Perforation")
dlg.addDoubleInput('TopPerf', 'TopPerf 1', 0, -2147483647, +2147483647, 1, 1, "help")
dlg.addDoubleInput('BopPerf', 'BopPerf 1', 0, -2147483647, +2147483647, 1, 1, "help")
dlg.execDialog()
topPerf = dlg.getDoubleInput('TopPerf')
botPerf = dlg.getDoubleInput('BopPerf')

for well in db.selectedWellList():
	dsLqc = 'LQC'
	db.variableCreate(well, dsLqc, 'PERF',2)
	md = db.variableLoad(well, dsLqc, db.referenceName(well, dsLqc))
	perf = db.variableLoad(well, dsLqc, 'PERF')
	perfList = []
	for i in range(len(md)):
		perf[i] = 0
		perfList.append(perf[i])
		if md[i] >= topPerf and md[i] <= botPerf:
			perf[i] = 1
			perfList[i] = (perf[i])
	db.variableSave(well, dsLqc, 'PERF', 'Perforation', 'unitless', perfList, 0, 'auto')
