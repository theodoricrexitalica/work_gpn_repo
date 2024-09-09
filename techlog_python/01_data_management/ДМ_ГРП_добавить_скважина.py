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

def dstNameFunc(well):
	dstNameList = []
	for ds in db.datasetList(well):
		if 'FRAC' in ds:
			dstNameList.append(1)
	if len(dstNameList) == 0:
		dstName = 'FRAC' + '_1'
	else:
		dstName = 'FRAC' + '_' + str(len(dstNameList)+1)
	return dstName

dlg = tda.dialogAdvanced("Perforation")
dlg.addDoubleInput('TopPerf_1', 'TopPerf', 0, -2147483647, +2147483647, 1, 1, "help")
dlg.addDoubleInput('BopPerf_1', 'BopPerf', 0, -2147483647, +2147483647, 1, 1, "help")
dlg.addTextInput('TextInp_1', 'Mprop...', 0)
dlg.addDoubleInput('TopPerf_2', 'TopPerf', 0, -2147483647, +2147483647, 1, 1, "help")
dlg.addDoubleInput('BopPerf_2', 'BopPerf', 0, -2147483647, +2147483647, 1, 1, "help")
dlg.addTextInput('TextInp_2', 'Mprop...', 0)
dlg.addDoubleInput('TopPerf_3', 'TopPerf', 0, -2147483647, +2147483647, 1, 1, "help")
dlg.addDoubleInput('BopPerf_3', 'BopPerf', 0, -2147483647, +2147483647, 1, 1, "help")
dlg.addTextInput('TextInp_3', 'Mprop...', 0)

dlg.execDialog()
topPerf_1 = dlg.getDoubleInput('TopPerf_1')
botPerf_1 = dlg.getDoubleInput('BopPerf_1')
text_1 = dlg.getTextInput('TextInp_1')
topPerf_2 = dlg.getDoubleInput('TopPerf_2')
botPerf_2 = dlg.getDoubleInput('BopPerf_2')
text_2 = dlg.getTextInput('TextInp_2')
topPerf_3 = dlg.getDoubleInput('TopPerf_3')
botPerf_3 = dlg.getDoubleInput('BopPerf_3')
text_3 = dlg.getTextInput('TextInp_3')


for well in db.selectedWellList():
	dstName = dstNameFunc(well)
	dstList = [topPerf_1, botPerf_1,topPerf_2, botPerf_2,topPerf_3, botPerf_3]
	dstList = [x for x in dstList if x != 0]
	txtList = [text_1, text_2, text_3]
	text = []
	perf = []
	for i in txtList:
		if len(i) == 0:
			pass
		else:
			perf.append(1)
			perf.append(-9999)
			text.append(i)
			text.append(-9999)
	db.datasetCreate(well, dstName, 'MD', 'Measured Depth', 'm', dstList, 'float')
	db.variableCreate(well, dstName, 'Overview', 1)
	db.variableSave(well, dstName, 'Overview', 'Remark', 'unitless', text, 0, 'string')
	db.variableFamilyChange(well, dstName, 'Overview', 'Remarks')
	db.variableTypeChange(well, dstName, 'Overview', 'RichText')
	db.variableSave(well,dstName, dstName, 'Perforation', 'unitless', perf, 0, 'auto')
	try:
		if db.datasetExists(well, 'ZONES_gm'):
			db.variableCopy(well, 'ZONES_gm', 'ZONES', dstName, 'ZONES', 'automatic')
		else:
			db.variableCopy(well, 'ZONES_bdntc', 'ZONES', dstName, 'ZONES', 'automatic')
	except:
		pass
	if db.variableExists(well, dstName, 'ZONES'):
		lastName = db.variableLoad(well, dstName, 'ZONES')
		lastName[-1] = -9999
		db.variableSave(well, dstName, 'ZONES', 'Zone Name', 'unitless', lastName)
	else:
		pass
