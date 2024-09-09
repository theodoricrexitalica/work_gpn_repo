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
__date__ = """2022-04-29"""
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
import win32com.client
import os
import TechlogStat as ts

def kng_avg (well):
	ds_rigis_gm = 'RIGIS_gm'
	ds_rigis_bd = 'RIGIS_bdntc'
	var_kng = 'kng'
	target_zone = 'БС9-2-1+2_TOP_S'
	zone_ds = 'ZONES_gm'
	ind1_gm = db.datasetZoneIndice(well, ds_rigis_gm, zone_ds, target_zone, 'Zone Name')[0]
	ind2_gm =  db.datasetZoneIndice(well, ds_rigis_gm, zone_ds, target_zone, 'Zone Name')[1]
	var_gm = db.variableLoad(well, ds_rigis_gm, var_kng)[ind1_gm:ind2_gm+1]
	var_gm_new = []
	for digit in var_gm:
		if digit > 0:
			var_gm_new.append(digit)
	ind1_bd = db.datasetZoneIndice(well, ds_rigis_bd, zone_ds, target_zone, 'Zone Name')[0]
	ind2_bd =  db.datasetZoneIndice(well, ds_rigis_bd, zone_ds, target_zone, 'Zone Name')[1]
	var_bd = db.variableLoad(well, ds_rigis_bd, var_kng)[ind1_bd:ind2_bd+1]
	var_bd_new = []
	for digit in var_bd:
		if digit > 0:
			var_bd_new.append(digit)
	return ts.mean(var_gm_new), ts.median(var_gm_new), ts.mean(var_bd_new), ts.median(var_bd_new)

Excel = win32com.client.Dispatch('Excel.Application')
wb =Excel.Workbooks.Open(u'e:\\OilFields\\Sugmutskoe\\req2604\\sugmur_kng.xlsx')
sheet = wb.ActiveSheet
cell_values = []
cell_rows = []
for row in range(2,991):
	values = sheet.Cells(row,1).value
	cell_values.append(values)
	cell_rows.append(row)
my_dict = dict(zip(cell_values, cell_rows))

for well in db.wellList()[:]:
	for well_excel in cell_values:
		well_excel_sug = well_excel.replace('611_', 'Sug-')
		if well == well_excel_sug:
			cell_rows = my_dict[well_excel]
			try:
				kng_avg(well)
				print(f'{well} is equal {well_excel} and cell row is {cell_rows} Kng = {kng_avg(well)[3]}')
				sheet.Cells(1,3).value = 'mean_gm'
				sheet.Cells(cell_rows,3).value = kng_avg(well)[0]
				sheet.Cells(1,4).value = 'median_gm'
				sheet.Cells(cell_rows,4).value = kng_avg(well)[1]
				sheet.Cells(1,5).value = 'mean_bdntc'
				sheet.Cells(cell_rows,5).value = kng_avg(well)[2]
				sheet.Cells(1,6).value = 'median_bdntc'
				sheet.Cells(cell_rows,6).value = kng_avg(well)[3]
				sheet.Cells(1,7).value = 'techlog well'
				sheet.Cells(cell_rows,7).value =well
			except:
				sheet.Cells(cell_rows,3).value = 'problem with rigis data'
wb.Save()
wb.Close()
Excel.Quit()

#for well in db.selectedWellList():
	#try:
		#print(well, kng_avg(well)[3])
	#except:
		#pass
