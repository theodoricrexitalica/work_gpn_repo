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
__date__ = """2021-12-21"""
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
cc = 0
zonation = "ZONES"
ds_reference_list = ["GDB_LOGS", "inclination", "Index", "LQC", "RIGIS_bdntc", "RIGIS_gm", "WH", zonation]
well_list = []
gbd_logs_well = []
gbd_cc = 0
inclination_well = []
inc_cc = 0
index_well = []
ind_cc = 0
lqc_well = []
lqc_cc = 0
bdntc_well = []
bdntc_cc = 0
gm_well = []
gm_cc = 0
wh_well = []
wh_cc = 0
zonation_well = []
zonation_cc = 0
for well in db.wellList():
	cc += 1
	well_list.append(well)
	ds_list = db.datasetList(well)
	if not ds_reference_list[0] in ds_list:
		gbd_cc += 1
		gbd_logs_well.append(well)
	if not ds_reference_list[1] in ds_list:
		inc_cc += 1
		inclination_well.append(well)
	if not ds_reference_list[2] in ds_list:
		ind_cc += 1
		index_well.append(well)
	if not ds_reference_list[3] in ds_list:
		lqc_cc += 1
		lqc_well.append(well)
	if not ds_reference_list[4] in ds_list:
		bdntc_cc += 1
		bdntc_well.append(well)
	if not ds_reference_list[5] in ds_list:
		gm_cc += 1
		gm_well.append(well)
	if not ds_reference_list[6] in ds_list:
		wh_cc += 1
		wh_well.append(well)
	if not zonation in ds_list:
		zonation_cc += 1
		zonation_well.append(well)
#well_list_clean = [item for item in well_list if item not in zonation_well]
#print("gbd_logs_well",gbd_cc) 
#print(gbd_logs_well)
#print("inclination_well",inc_cc) 
#print(inclination_well)

#print("index_well", ind_cc) 
#for i in index_well:
	#print(i)

#print("lqc_well", lqc_cc) 
#print(lqc_well)

print("zonation_well", zonation_cc) 
for i in zonation_well:
	print(i)

#print("gm_well", gm_cc) 
#for i in gm_well:
	#print(i)

#print("well_count", cc)
#print(well_list_clean)
