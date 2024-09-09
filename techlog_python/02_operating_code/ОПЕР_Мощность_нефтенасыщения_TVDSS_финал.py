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

__author__ = """Taras DOLGUSHIN (Dolgushin.TYu)"""
__date__ = """2021-07-21"""
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
s = ';'
def heff_satur(well, ds, zone, sat_code):
	round_range = 4
	db.variableCopy(well, "Index", "TVDSS", ds, "TVDSS", "anti-aliasing", "project", "project", -1, 0, 1)
	db.variableCopy(well, zonation, "ZONES", ds, "ZONES", "automatic", "project", "project", -1, 0, 1)
	tvdss = db.variableLoad(well, ds, "TVDSS")
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	satur =  db.variableLoad(well, ds, "satur")
	zones = db.variableLoad(well, ds, "ZONES")
	top_tvdss = []
	bot_tvdss = []
	top_md = []
	bot_md = []
	for i in range(len(tvdss)):
		if zones[i] == zone and satur[i] == sat_code:
			if satur[i] == sat_code and satur[i-1] != sat_code:
				top_tvdss.append(round(tvdss[i],1))
				top_md.append(round(md[i],1))
			try:
				if satur[i] == sat_code and satur[i+1] != sat_code:
					bot_tvdss.append(round(tvdss[i],1) + 0.1)																	
					bot_md.append(round(md[i],1) + 0.1)
			except:
				bot_tvdss.append(tvdss[i])
				bot_md.append(md[i])
	#print(top_tvdss)
	#print(bot_tvdss)
	h_eff_list_tvdss = []
	h_eff_list_md = []
	for j in range(len(top_tvdss)):
		h_eff_tvdss = bot_tvdss[j] - top_tvdss[j]
		h_eff_tvdss = round(h_eff_tvdss, round_range)
		h_eff_list_tvdss.append(h_eff_tvdss)
		h_eff_md = bot_md[j] - top_md[j]
		h_eff_md = round(h_eff_md, round_range)
		h_eff_list_md.append(h_eff_md)
	return ([well, 
				round(sum(h_eff_list_tvdss), round_range),
				round(sum(h_eff_list_md), round_range),
				sat_code])

print('well', 'h_eff_tvdss', 'h_eff_md', 'total_h_tvdss', 'sat_code',)
for well in db.selectedWellList():
	zone1 = 'БС10-2_TOP_S'																				#указать зонейшен
	#zone2 = 'ЮВ1-2-Б_TOP_S'
	ds = "RIGIS_slb"																								#указать датасет с РИГИС
	zonation = "ZONES_gm"																				#указать датасет с ЗОНАМИ
	
	h10 = heff_satur(well, ds, zone1, 10)
	h8 = heff_satur(well, ds, zone1, 8)
	h6 =  heff_satur(well, ds, zone1, 6)
	h2 = heff_satur(well, ds, zone1, 2)

	#print(h8[0], h8[1], h8[2], h8[3], round(h10[1] + h8[1] + h6[1] + h2[1],1))			#Надо редактировать какие наборы данных использовать для суммирования
	print(h6[0], h6[1], h6[2], round(h10[1] + h8[1] + h6[1] + h2[1],1), h6[3],)
	#print(h10[0], h10[1], h10[2], round(h10[1] + h8[1] + h6[1] + h2[1],1), h6[3],)
	print(h2[0], h2[1], h2[2], h2[3], round(h10[1] + h8[1] + h6[1] + h2[1],1))
	
#Коды насыщения	
#1	Вода + Нефть
#2	Вода
#3	Газ
#4	Газ + Нефть
#5	Вода пресная в интервале обводнения
#6	Неясно
#7	Не определено
#8	Нефть
#9	Нефть ПН
#10	Нефть + Вода
#11	Продукт
#12	Вода минерализованная в интервале обводнения
#13	Возможно продукт
#14	Нефть при отдаче
#0	Неколлектор
#15	Газ + Вода
#18	Нефть + Газ
#20	Вода + Газ
#19	Нефть + Газовый фактор
#16	Легкий углеводород
#17	Легкий углеводород + Вода
#25	Вода + Продукт
#22	Газоконденсат
#23	Нефть ПН1
#24	Нефть ПН2
#21	Вода пластовая
#26	Нефть+Вода+Газ
#27	ПРОДУКТ + ВОДА
#28	ОБВОДНЕНИЕ (В НЕФТЬ)
#30	Вода + следы нефти
#31	Нефть + следы газа
#29	Битум
#34	Признак нефти
#32	Углекислый газ
#33	Остаточная нефть
