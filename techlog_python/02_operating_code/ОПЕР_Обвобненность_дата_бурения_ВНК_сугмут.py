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
__date__ = """2022-03-22"""
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
import datetime as dt
import statistics as stat

ds_mer = 'MER'
ds_perf = 'PERF'
ds_rigis = 'RIGIS_bdntc'
month = 3
well_list = []
tvdss_perf_bot = []
watercut_avg = []
date = []
var_target = ['DATE_1']
s = ';'

def perf_data_detection(well, ds, var_target):
	completion_date = db.variableLoad(well, ds, var_target[0])
	completion_date_list = []
	for date_srt in completion_date:
		try:
			completion_date_list.append(dt.datetime.strptime(str(date_srt), '%d.%m.%Y'))
		except:
			pass
	completion_date_list.sort()
	date_final = str(completion_date_list[0])
	#print(well, s, date_final.split(' ')[0])
	return date_final.split(' ')[0]

for well in db.selectedWellList():
	if db.datasetExists(well, ds_mer) and db.datasetExists(well, ds_perf) and  db.datasetExists(well, ds_rigis):
		ref_name = db.referenceName(well, ds_rigis)
		var_perf = db.variableLoad(well, ds_rigis, 'PERF')
		md = db.variableLoad(well, ds_rigis, ref_name)
		tvdss = db.variableLoad(well, ds_rigis, 'TVDSS')
		oil = stat.mean(db.variableLoad(well, ds_mer, 'v_oil')[0:month])
		water = stat.mean(db.variableLoad(well, ds_mer, 'v_water')[0:month])
		water_list = db.variableLoad(well, ds_mer, 'v_water')[0:month]
		print(water_list)
		for i in range(len(md)):
			if var_perf[i] == 1 and var_perf[i+1] != 1:
				well_list.append(well)
				tvdss_perf_bot.append(round(tvdss[i],1))
				watercut_avg.append(round(water/(oil+water),2))
				date.append(perf_data_detection(well, ds_perf, var_target))

##print(tvdss_perf_bot, well_list)
#dict_perf = dict(zip(tvdss_perf_bot,well_list))																#Создание словаря из списков скважин и глубин перфорации
#list_keys = list(dict_perf.keys())
#list_keys.sort()																												#Сортировка ключей словаря
#list_keys.reverse()
#for i in range(len(list_keys)):
	#print(dict_perf[list_keys[i]], list_keys[i])
for i in range(len(well_list)):
	print(well_list[i], tvdss_perf_bot[i], watercut_avg[i], date[i])
