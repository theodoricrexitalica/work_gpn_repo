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

__doc__ = """Надо сохранить эксель-файл как  csv с разделителями табуляции и запустить скрипт."""
__author__ = """Taras DOLGUSHIN (dolgushin.tyu)"""
__date__ = """2021-11-21"""
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
import datetime
import TechlogDialogAdvanced as tda
from itertools import groupby

tempFile = rtc.getOpenFileName("Well Tops", multiselect = True, filter = ["All files;*.*"])
db.currentChange("import")
wells_txt = [] 
data_txt = []
#with open(tempFile, "r", -1, "ansi") as file:
with open(tempFile[0], "r", -1, "ansi") as file:
	for line in file.readlines()[1:]:
		line = line.replace("\n", "")
		well_name = line.split(";")[0]
		wells_txt.append(well_name)
		data = line.split(";")[1:]
		data_txt.append(data)
#print(wells_txt)
#print(data_txt)

db.currentChange("import")
current_date = datetime.datetime.now()
ds = 'MER_' + (current_date.strftime("%b%y"))								#Формирование имени датасета с МЭРами согласно текущему месяцу загрузки

for i in range(len(wells_txt)):
	db.wellCreate(wells_txt[i])
for well in db.wellList():
	ref = []
	month = []
	type = []
	zone  = []
	work = []
	esp = []
	comment = []
	work_hrs = []
	standby_hrs = []
	oil = []
	water = []
	v_oil = []
	v_water = []
	inj_water = []
	opd = []
	wpd = []
	wct = []
	wcv = []
	cc_ref = 0
	for i in range(len(wells_txt)):
		if well == wells_txt[i]:
			cc_ref += 1																				#Счетчик для индекса датасета, обновляется на каждой скважине
			try:
				ref.append(cc_ref)
				month.append(data_txt[i][0])
				zone.append(data_txt[i][1])
				type.append(data_txt[i][2])
				work.append(data_txt[i][3])
				esp.append(data_txt[i][4])
				comment.append(data_txt[i][5])
				work_hrs.append(float(data_txt[i][6]))
				standby_hrs.append(float(data_txt[i][8]))
				oil.append(float(data_txt[i][9]))
				water.append(float(data_txt[i][10]))
				v_oil.append(float(data_txt[i][15]))
				v_water.append(float(data_txt[i][16]))
				
				try:
					opd_calc = ((float(data_txt[i][9]))/(float(data_txt[i][6])))*24
					opdv_calc = ((float(data_txt[i][15]))/(float(data_txt[i][6])))*24
				except:
					opd_calc = 0
					opdv_calc = 0
				try:
					wpd_calc = ((float(data_txt[i][10]))/(float(data_txt[i][6])))*24
					wpdv_calc = ((float(data_txt[i][16]))/(float(data_txt[i][6])))*24
				except:
					wpd_calc = 0
					wpdv_calc = 0
				opd.append(opd_calc)
				wpd.append(wpd_calc)
				try:
					wct_calc = (wpd_calc/(wpd_calc + opd_calc))
				except:
					wct_calc = 0
				wct.append(wct_calc*100)
				#try:
					#wcv_calc = (wpdv_calc/(wpdv_calc + opdv_calc))
				#except:
					#wcv_calc = 0
				#wcv.append(wcv_calc*100)
				try:
					inj_calc = ((float(data_txt[i][20]))/(float(data_txt[i][6])))*24
				except:
					inj_calc = 0
				inj_water.append(inj_calc)
			except:
				pass

	db.datasetCreate(well, ds, "Ref", "Reference", "m", ref, "double")
	db.datasetTypeChange(well, ds, "continuous")
	db.variableSave(well, ds, "01_month", "", "", month, 0, "auto")
	db.variableUnitChange(well, ds, "01_month", "unitless")
	db.variableSave(well, ds, "02_zone", "", "", zone, 0, "auto")
	db.variableUnitChange(well, ds, "02_zone", "unitless")
	db.variableSave(well, ds, "03_type", "", "", type, 0, "auto")
	db.variableUnitChange(well, ds, "03_type", "unitless")
	db.variableSave(well, ds, "04_work", "", "", work, 0, "auto")
	db.variableUnitChange(well, ds, "04_work", "unitless")
	db.variableSave(well, ds, "05_esp", "", "", esp, 0, "auto")
	db.variableUnitChange(well, ds, "05_esp", "unitless")
	db.variableSave(well, ds, "06_comment", "", "", comment, 0, "auto")
	db.variableUnitChange(well, ds, "06_comment", "unitless")
	db.variableSave(well, ds, "07_work_hrs", "", "", work_hrs, 0, "auto")
	db.variableUnitChange(well, ds, "07_work_hrs", "hrs")
	db.variableSave(well, ds, "08_standby_hrs", "", "", standby_hrs, 0, "auto")
	db.variableUnitChange(well, ds, "08_standby_hrs", "hrs")
	db.variableSave(well, ds, "09_oil", "", "", oil, 0, "auto")
	db.variableUnitChange(well, ds, "09_oil", "t")
	db.variableSave(well, ds, "10_water", "", "", water, 0, "auto")
	db.variableUnitChange(well, ds, "10_water", "t")
	db.variableSave(well, ds, "11_v_oil", "", "", v_oil, 0, "auto")
	db.variableUnitChange(well, ds, "11_v_oil", "m3")
	db.variableSave(well, ds, "12_v_water", "", "", v_water, 0, "auto")
	db.variableUnitChange(well, ds, "12_v_water", "m3")
	db.variableSave(well, ds, "13_opd", "", "", opd, 0, "auto")
	db.variableUnitChange(well, ds, "13_opd", "t/d")
	db.variableSave(well, ds, "14_wpd", "", "", wpd, 0, "auto")
	db.variableUnitChange(well, ds, "14_wpd", "t/d")
	db.variableSave(well, ds, "15_wct", "", "", wct, 0, "auto")
	db.variableUnitChange(well, ds, "15_wct", "%")
	#db.variableSave(well, ds, "15_wcv", "", "", wcv, 0, "auto")
	#db.variableUnitChange(well, ds, "15_wcv", "%")
	db.variableSave(well, ds, "16_inj", "", "", inj_water, 0, "auto")
	db.variableUnitChange(well, ds, "16_inj", "m3/d")
	


db.currentChange('project')
well_name = []
ngt_name = []
for well in db.wellList():																							#Чтение имени NGT в датасете скважины и формирование списков
	ds_wi = 'wellinfo'
	var_wi = 'well_ngt'
	if db.datasetExists(well, ds_wi):
		ngt_name_var= db.variableLoad(well, ds_wi, var_wi)
		well_name.append(well)
		ngt_name.append(ngt_name_var[0])
dict_wells = dict(zip(ngt_name, well_name))															#Создание словаря из 2х списков

db.currentChange('import')
for well_imported in db.wellList():
	for well_ngt in dict_wells:																						#Поиск совпадения ключей словаря со названиями скважин в импорте
		if well_ngt == well_imported:
			db.wellRename(well_ngt, dict_wells[well_ngt])
			print(well_ngt, dict_wells[well_ngt])
