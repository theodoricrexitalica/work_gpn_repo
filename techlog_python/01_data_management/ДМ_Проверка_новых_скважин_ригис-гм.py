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
__date__ = """2022-10-27"""
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
import RussianTools.RussianTools_Common as rtc
from os import listdir
from os.path import isfile, join

path =db.dirUser()
file_name = 'TarasOutput.txt'
file_path = os.path.join(path, file_name)
with open(file_path, 'a') as file:
		file.truncate(0)

tempFile = rtc.getOpenFileName("Rigis", multiselect = True, filter = ["All files;*.*"])
myPath = ('\\'.join(tempFile[0].split('\\')[:-1]))

onlyfiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
uwiNameList = onlyfiles
uwiName = list(uwiNameList)[0].split('_')[0]
func = lambda x: x.split('.')[0]
onlyfiles = map(func, onlyfiles)
for well in db.wellList()[:5]:
	if '-' in well:
		fieldName = well.split('-')[0]
func = lambda x: fieldName + '-' + x.split('_')[1]
uploadName = map(func, onlyfiles)

try:
	tempVar = myPath.split('\\')[:4]
	tempVar.append('rigis_bdntc')
	myPath_bdntc = ('\\'.join(tempVar))
	onlyfiles_bdntc = [f for f in listdir(myPath_bdntc) if isfile(join(myPath, f))]
	func = lambda x: x.split('.')[0]
	onlyfiles_bdntc = map(func, onlyfiles_bdntc)
	func = lambda x: fieldName + '-' + x.split('_')[1]
	uploadName_bdntc = map(func, onlyfiles_bdntc)
except:
	uploadName_bdntc = [0]
	
delta = set(uploadName) - set(db.wellList())
delta_bdntc = set(uploadName_bdntc) - set(db.wellList())
delta = list(delta) + list(delta_bdntc)
if len(delta) > 0:
	for names in delta:
		print(uwiName + '_' + names.split('-')[1] + ',')
		lines = [uwiName + '_' + names.split('-')[1] + ',' + '\n']
		with open(file_path, 'a', encoding = 'ansi') as file:
			for line in lines:
				file.write(line)
	os.startfile(file_path)
else:
	print('New wells are absent')
