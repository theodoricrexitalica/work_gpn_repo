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
s = ";"
#Если надо обновить зонейшен в PT_RIGIS, надо запустить 2 строчки ниже
#for well in db.selectedWellList():
	#print(well, db.variableCopy(well, "ZONES_sut_bs11_10", "ZONES", "PT_RIGIS", "ZONES", "automatic", "project", "project", -1, False, True))

print("well",s,"h_eff", s, "code")
for well in db.selectedWellList():
	ds = "PT_RIGIS"
	md = db.variableLoad(well, ds, db.referenceName(well, ds))
	satur =  db.variableLoad(well, ds, "satur")
	zones = db.variableLoad(well, ds, "ZONES")
	top_md = []
	bot_md = []
	satur_code = 8
	for i in range(len(md)):
		if zones[i] == "БС11-10_TOP_S" and satur[i] == satur_code:
			if satur[i] == satur_code and satur[i-1] != satur_code:
				top_md.append(md[i])
			try:
				if satur[i] == satur_code and satur[i+1] != satur_code:
					bot_md.append(md[i])
			except:
				bot_md.append(md[i])
	h_eff_list = []
	for j in range(len(top_md)):
		h_eff = bot_md[j] - top_md[j]
		h_eff = round(h_eff,1)
		h_eff_list.append(h_eff)
	if sum(h_eff_list) > 0:
		print(well, s, round(sum(h_eff_list),1), s, satur_code)



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
