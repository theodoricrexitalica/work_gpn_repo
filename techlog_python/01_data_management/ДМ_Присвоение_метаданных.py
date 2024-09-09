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
__date__ = """2022-05-12"""
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

for well in db.selectedWellList():
	ds_wh = 'WH'
	ds_wi = 'wellinfo'
	ds_status = 'wellstatus'
	var_prod_start = 'production_start'
	var_drill_fin = 'drilling_fin'
	var_ngt_name = 'well_ngt'																									#Можно указать какую переменную смотрим
	var_stat = 'well_status'
	var_stat_dt = 'date'
	try:
		x = int(db.variableLoad(well, ds_wh, 'X-Coord')[0])
		y = int(db.variableLoad(well, ds_wh, 'Y-Coord')[0])
		db.wellPropertyChange(well, 'X', str(x), 'm', 'from WH dataset')
		db.wellPropertyChange(well, 'Y', str(y), 'm', 'from WH dataset')
		print(well, x, y, ngt_name)
	except:
		pass

	if (db.datasetExists(well, ds_wi) 
		and db.variableLoad(well, ds_wi, var_drill_fin)[0] != '' 
		and db.variableLoad(well, ds_wi, var_drill_fin)[0] != -9999):													#Проверка наличия датасета, пустой строки или -9999
		prod_start = db.variableLoad(well, ds_wi, var_prod_start)[0]
		drill_fin = db.variableLoad(well, ds_wi, var_drill_fin)[0]
		db.wellPropertyChange(well, 'SPUD_date', drill_fin, '','Бурение окончено')
		db.wellPropertyChange(well, 'Completion_date', prod_start, '','Освоение окончено')
		print(well, drill_fin, prod_start)
	else:
		pass
	if db.datasetExists(well, ds_wi):
		ngt_name = db.variableLoad(well, ds_wi, var_ngt_name)[0]
		db.wellPropertyChange(well, 'Short_well_name', ngt_name, '','Имя скважины NGT')
	else:
		pass
	if db.datasetExists(well, ds_status):
		status_date = db.variableLoad(well, ds_status, var_stat_dt)[0]
		status = db.variableLoad(well, ds_status, var_stat)[0]
		db.wellPropertyChange(well, 'Status', str(status), '',str(status_date))
	else:
		pass
	
	try:
		if type(db.variableLoad(well, 'WH', 'Pad')[0]) == str:
			padName = well + '-K' + db.variableLoad(well, 'WH', 'Pad')[0]
		else:
			padName = well + '-K' + str(int(db.variableLoad(well, 'WH', 'Pad')[0]))
	except:
		padName = well +'-NA'
	db.wellPropertyChange(well, 'Long_well_name', padName, '', '')
	#print(well, x, y, ngt_name, drill_fin, prod_start)
