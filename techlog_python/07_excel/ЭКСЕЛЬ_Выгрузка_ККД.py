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
__date__ = """2022-09-16"""
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
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import RussianTools.RussianTools_Common as rtc
import win32com.client

tempFile = rtc.getOpenFileName("Well Tops", multiselect = True, filter = ["All files;*.*"])

excel = win32com.client.Dispatch('excel.application')
wb = excel.Workbooks.Open(tempFile[0])
s = '|'
lab_number = []
phit = []
perm = []
print(tempFile[0])
print ('MD | Lab_number | KPVK | KPRK | PCWGK | PCWOK | KVK | Lithology')
print ('m | unitless | % | mD | kgs/cm2 | kgs/cm2 | % | unitless')

for sheet in wb.Sheets:
	lab_number = sheet.Cells(5, 7).value
	phit = sheet.Cells(5, 8).value
	perm = sheet.Cells(5, 9).value
	interval = float((sheet.Cells(2, 7).value).split('-')[0])
	md_inc = float(sheet.Cells(2, 9).value)
	sample_md = interval + md_inc
	litho = str(sheet.Cells(5, 1).value)
	for j in range(8,17):
		pc_wg = sheet.Cells(j, 7).value
		pc_wo = sheet.Cells(j, 8).value
		sw =  sheet.Cells(j, 9).value
		print(sample_md, s, 
				lab_number, s, 
				phit, s, 
				perm, s,
				pc_wg, s,
				pc_wo, s,
				sw, s,
				litho)
