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
__date__ = """2022-04-15"""
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
import os
import re

path = r'\\tmn-ntc-filer3\ARCH_KERN\ARCH_NNG\\Сугмутское'					#Здесь меняем название месторождения на сервере, где нранится керна
def files(path):
	for dir in os.listdir(path):
		if os.path.isdir(os.path.join(path, dir)):
			yield dir

well_core_server = []
for dir in files(path):
	well_core_server.append(dir)
well_core_server = well_core_server[:-1]														#Строка, чтоб исключить из списка каталоги, в названии которых нет цифр
func = lambda x: re.findall(r'\d+', x)[0]																#Функция для регэкспа цифр из названий каталогов с керном на сервере
well_core_server = list(map(func, well_core_server))

func = lambda x: x.split('-')[1]
well_list = map(func, db.wellList())
func = lambda x: re.findall(r'\d+', x)[0]																#Функция для регэкспа цифр из названий скважин в базе
well_list = list(map(func, well_list))


result = list(set(well_core_server) - set(well_list))
#result =list( set(well_list) -  set(well_core_server) )
result.sort()
print('well w/ core on server:', len(well_core_server))
print('well in GeoDB:', len(well_list))
print('wells on server but not in GeoBD')
print(result)
print('wells on server but not in GeoBD:', len(result))
