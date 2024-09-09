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
__date__ = """2022-09-30"""
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
#g_cc = 0
#st_cc = 0
#for well in db.selectedWellList():
	#if 'G' in well:
		#g_cc += 1
	#else:
		#st_cc += 1

#print('g_cc', g_cc)
#print('st_cc', st_cc)
#print('total', g_cc + st_cc)

#g_cc 46
#st_cc 33
#total 79

def rigis_top_bot(well, ds):
	if db.datasetExists(well, ds):
			mdTopRigis = db.variableLoad(well, ds, db.referenceName(well, ds))[10]
			mdBotRigis = db.variableLoad(well, ds, db.referenceName(well, ds))[-1]
	else:
		mdBotRigis = ' rigis_na'
		mdTopRigis = ' rigis_na'
	return mdTopRigis, mdBotRigis
	
def logs_btm(well, ds, var):
	if db.variableExists(well, ds, var):
			logsBot = db.variableInformation(well, ds, var, 'BottomIndex')
			mdLqc = db.variableLoad(well, ds, db.referenceName(well, ds))
			botIndVar = mdLqc[int(logsBot)]
	else:
		botIndVar = 'varBot_na'
	return botIndVar
	
#def logs_data(well, dsSrc, dsDst, catVar, logName):
	#try:
		#log_data = []
		#cat_data = []
		#md_data = []
		#tvdss_data = []
		#db.variableCopy(well, dsSrc, catVar, dsDst, catVar, 'automatic')
		#log = db.variableLoad(well, dsDst, logName)
		#cat = db.variableLoad(well, dsDst, catVar)
		#md =  db.variableLoad(well, dsDst, db.referenceName(well, dsDst))
		#tvdss =  db.variableLoad(well, dsDst, 'TVDSS')
		#for i in range(len(cat)):
			#if cat[i] != -9999.0:
				#log_data.append(log[i])
				#cat_data.append(cat[i])
				#md_data.append(md[i])
				#tvdss_data.append(tvdss[i])
		#db.variableDelete(well, dsDst, catVar)
	#except:
		#print(well, 'problem in func')
	#return zip(log_data, cat_data, md_data, tvdss_data)

dsZone = 'ZONES_va'
dsRigis = 'RIGIS_gm'
dsLqc = 'LQC'
header = [ 'well', 'zone', 'rigis_top', 'rigis_bot', 'GR', 'RT_SH', 'lit', 'md', 'tvdss']

import csv
with open('E://data.csv', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	
	for well in db.wellList():
		if 'G' in well:
			target_zone = db.variableLoad(well, dsZone, 'ZONES')[-1]
			
			lqc_top_bot = rigis_top_bot(well, dsRigis)
			botGR = logs_btm(well, dsLqc, 'GR')
			botRTSH = logs_btm(well, dsLqc, 'RT_SH')
			
			logsGR = logs_data(well,  'RIGIS_gm', 'LQC', 'lit', 'GR')
			logsRT = logs_data(well,  'RIGIS_gm', 'LQC', 'lit', 'RT_SH')
			try:
				gr, cat_data, md_data, tvdss_data = zip(*logsGR)
				rt, cat_data, md_data, tvdss_data = zip(*logsRT)
			except:
				print(well, 'problem with zip')
				pass
			
			try:
				for i in range(len(gr)):
					lines =[well, target_zone, lqc_top_bot[0], lqc_top_bot[1], gr[i], rt[i], 
								cat_data[i], md_data[i], tvdss_data[i]]
					writer.writerow(lines)
			except:
				print(well, 'problem with data in csv')
				pass
