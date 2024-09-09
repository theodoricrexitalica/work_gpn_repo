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
def Heff(well, ds):
	broken_wells_infunction = []
	if db.datasetExists(well, ds):
		db.variableCopy(well, "Index", "TVDSS", ds, "TVDSS", "anti-aliasing", "project", "project", -1 , 0, 1)
		db.variableCopy(well, zonation, "ZONES", ds, "ZONES", "automatic", "project", "project", -1 , 0, 1)
		tvdss = db.variableLoad(well, ds, "TVDSS")
		#tvdss = db.variableLoad(well, ds, db.referenceName(well, ds)) #Если нет TVDSS в датасете, берем MD	
		lit =  db.variableLoad(well, ds, "lit")
		zones = db.variableLoad(well, ds, "ZONES")
		top_tvdss = []
		bot_tvdss = []
		lit_code = 1
		zones_ind = []
		for i in range(len(tvdss)):
			if zones[i] == zone:
				zones_ind.append(i)
		ind_top = zones_ind[0]
		if lit[ind_top] == lit_code and  lit[ind_top-1] != 0 :
			top_tvdss.append(round(tvdss[ind_top],1))
		else:
			pass
		for i in range(len(tvdss)):
			if zones[i] == zone:
				if lit[i] == lit_code and lit[i-1] != lit_code:
					top_tvdss.append(round(tvdss[i],1))
				try:
					if lit[i] == lit_code and lit[i+1] != lit_code:
						bot_tvdss.append(round(tvdss[i],2))
				except:
					bot_tvdss.append(tvdss[i])
		h_eff_list = []
		#print("top_tvdss", ds, top_tvdss)
		#print("bot_tvdss", ds,bot_tvdss)
		for j in range(len(top_tvdss)):
			h_eff = bot_tvdss[j] - top_tvdss[j]
			h_eff = round(h_eff,1)
			h_eff_list.append(h_eff)
		#print(well, s, ds, s, round(sum(h_eff_list),1), s, zone, s, lit_code)
	else:
		pass
	return [well, ds, round(sum(h_eff_list),1), zone]

s = ";"
broken_wells = []
print("well",s,"dataset", s,"h_eff", s, "zone", s, "diff_gm-bdntc",)
for well in db.selectedWellList():
	if "G" in well.split("-")[1]:
		pass
	else:
		try:
			zonation = "ZONES_vyng_bdntc"																												#менять датасет с ЗОНАМИ
			zone = "BV_5_TOP_S"																																#указать зону интереса
			ds_bdntc = "RIGIS_bdntc"	
			print(Heff(well, ds_bdntc)[0], s, Heff(well, ds_bdntc)[1], s, Heff(well, ds_bdntc)[2], s, Heff(well, ds_bdntc)[3])		#команды для тестирования RIGIS_bdntc
																										
			ds_gm = "RIGIS_gm"																																	#менять датасет с РИГИС
			#print(Heff(well, ds_gm))																																#команды для тестирования RIGIS_gm
		except:
			broken_wells.append(well)
print("broken wells list", broken_wells)
