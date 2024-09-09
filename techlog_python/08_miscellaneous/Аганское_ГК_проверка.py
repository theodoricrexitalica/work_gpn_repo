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
__date__ = """2022-12-07"""
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
print('quantity of wells:', len(db.wellList()))
cc_gr_no = 0
for well in db.wellList()[:]:
	for ds in db.datasetList(well):
		cc_gr = 0
		gr_list = []
		for var in db.variableList(well, ds):
			if 'GR' in var:
				cc_gr += 1
				gr_min = round(int(db.variableInformation(well, ds, var, 'TopIndex')),0)
				gr_max = round(int(db.variableInformation(well, ds, var, 'BottomIndex')),0)
				md = db.variableLoad(well, ds, db.referenceName(well, ds))
				delta = str(gr_max-gr_min)
				md_top = str(round(md[gr_min],0))
				md_bot = str(round(md[gr_max],0))
				gr_list.append(var + ':' + md_top + '-' + md_bot)
		print(well, gr_list, cc_gr)
		
		if len(gr_list) == 0:
			cc_gr_no += 1
print(cc_gr_no)
				
