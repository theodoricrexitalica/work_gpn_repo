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
__date__ = """2022-02-03"""
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
colour_list = ["#00FFFF",
"#7FFFD4",
"#0000FF",
"#8A2BE2",
"#A52A2A",
"#DEB887",
"#5F9EA0",
"#7FFF00",
"#D2691E",
"#FF7F50",
"#6495ED",
"#FFF8DC",
"#DC143C",
"#00FFFF",
"#00008B",
"#008B8B",
"#B8860B",
"#A9A9A9",
"#006400",
"#BDB76B",
"#8B008B",
"#556B2F",
"#FF8C00",
"#9932CC",
"#8B0000",
"#E9967A",
"#8FBC8F",
"#483D8B",
"#2F4F4F",
"#00CED1",
"#9400D3",
"#FF1493",
"#00BFFF",
"#696969",
"#1E90FF",
"#B22222",
"#228B22",
"#FF00FF",
"#DCDCDC",
"#FFD700",
"#DAA520",
"#008000",
"#ADFF2F",
"#FF69B4",
"#CD5C5C",
"#4B0082",
"#F0E68C",
"#E6E6FA",
"#7CFC00",
"#ADD8E6",
"#F08080",
"#E0FFFF",
"#FAFAD2",
"#D3D3D3",
"#90EE90",
"#FFB6C1",
"#FFA07A",
"#20B2AA",
"#87CEFA",
"#B0C4DE",
"#00FF00",
"#32CD32",
"#FF00FF",
"#800000",
"#66CDAA",
]

cc = 0
delta = 3
for well in db.selectedWellList():
	cc += delta
	print(well, colour_list[cc], cc)
	db.wellColorChange(well, colour_list[cc])
	#db.wellColorChange(well, "#808080")
