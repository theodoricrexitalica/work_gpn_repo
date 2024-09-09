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
__date__ = """2022-12-02"""
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
dictFam = {'P06H' : 'Extra Shallow Resistivity', 'P10H' : 'Shallow Resistivity', 'P22H' : 'Medium Resistivity', 'P28H' : 'Deep Resistivity', 'P34H' : 'Extra Deep Resistivity',
				  'RPCHM' : 'Shallow Resistivity', 'RPCLM' : 'Deep Resistivity', 'RPCECHM' : 'Shallow Resistivity', 'RPCECLM' : 'Deep Resistivity',
				  'R12PC' : 'Shallow Resistivity',  'R20PC' : 'Medium Resistivity', 'R28PC' : 'Deep Resistivity', 'R44PC' : 'Extra Deep Resistivity',
				  'R09PC' : 'Extra Shallow Resistivity', 'R15PC' : 'Shallow Resistivity', 'R27PC' : 'Medium Resistivity', 'R39PC' : 'Extra Deep Resistivity',
				  'RPSH' : 'Shallow Resistivity', 'RPLH' : 'Deep Resistivity',
				  'RPS2' : 'Shallow Resistivity', 'RPM2' : 'Medium Resistivity', 'RPD2' : 'Deep Resistivity',
				  'P33H' : 'Shallow Resistivity', 'P33L' : 'Deep Resistivity',
				  'RP06H' : 'Shallow Resistivity', 'RP10H' : 'Deep Resistivity',
				  'RPCECLX' : 'Deep Resistivity', 'RPCECSHX' : 'Shallow Resistivity',
				  'N2MPM' : 'Extra Shallow Resistivity', 'N4KPM' : 'Shallow Resistivity', 'F2MPM' : 'Medium Resistivity', 'F4KPM' : 'Deep Resistivity',
				  'CEDP':'Deep Resistivity', 'CEMP':'Medium Resistivity', 'CESP':'Shallow Resistivity',
				  'SEDP':'Deep Resistivity', 'SEMP':'Medium Resistivity', 'SESP':'Shallow Resistivity','SEXP' : 'Extra Shallow Resistivity',
				  'RPLL':'Deep Resistivity', 'RPSH':'Shallow Resistivity',
				  'F4KPM':'Deep Resistivity', 'F2MPM':'Medium Resistivity', 'N4KPM':'Shallow Resistivity','N2MPM' : 'Extra Shallow Resistivity'}

dictFamRnm = {'Extra Shallow Resistivity':'RT_ES', 'Shallow Resistivity':'RT_SH', 'Medium Resistivity':'RT_MD', 'Deep Resistivity':'RT_DP', 'Extra Deep Resistivity':'RT_ED'}

for well in db.selectedWellList():
	dsLqc = 'LQC'
	for var in db.variableList(well, dsLqc):
		if var != db.referenceName(well, dsLqc) and 'GR' not in var:
			db.variableFamilyChange(well, dsLqc, var, '')
	for key in dictFam.keys():
		for var in db.variableList(well, dsLqc):
			if key == var:
				db.variableFamilyChange(well, dsLqc, var, dictFam[key])
	for var in db.variableList(well, dsLqc):
		if db.variableFamily(well, dsLqc, var) == '':
			db.variableDelete(well, dsLqc, var)
	for famKey in dictFamRnm.keys():
		for var in db.variableList(well, dsLqc):
			if famKey == db.variableFamily(well, dsLqc, var):
				db.variableRename(well, dsLqc, var, dictFamRnm[famKey])
		
	for var in db.variableList(well, dsLqc):
		wrong_gr = "HAGRT"
		if db.variableExists(well, dsLqc, wrong_gr):
			db.variableFamilyChange(well, dsLqc, wrong_gr, "Gamma Ray")
			db.variableUnitChange(well, dsLqc, wrong_gr, "gapi")
		md = db.variableLoad(well, dsLqc, db.referenceName(well, dsLqc))

list_md = []																										#поиск самой длинной ГК в датасете ГС
list_var = []
for well in db.selectedWellList():
	dsLqc = 'LQC'
	wrong_gr = "HAGRT"
	if db.variableExists(well, dsLqc, wrong_gr):
		db.variableFamilyChange(well, dsLqc, wrong_gr, "Gamma Ray")
		db.variableUnitChange(well, dsLqc, wrong_gr, "gapi")
	md = db.variableLoad(well, dsLqc, db.referenceName(well, dsLqc))
	for var in db.variableList(well, dsLqc):
		if "Gamma" in db.variableFamily(well, dsLqc, var):
			ind = int(db.variableInformation(well, dsLqc,var, "BottomIndex"))
			list_md.append(md[ind])
			list_var.append(var)
dict_gr = dict(zip(list_md, list_var))
max_key =max(dict_gr.keys())
var_gr_max = dict_gr[max_key] 																#поиск названия переменной с максимальной длинной по стволу
#print(well, var_gr_max, max_key, "m", "max_depth is", md[-1])

for well in db.selectedWellList():
	for var_delete in list_var:
		if var_delete != var_gr_max:
			db.variableDelete(well, dsLqc, var_delete)
	db.variableFamilyChange(well, dsLqc, var_gr_max, "Gamma Ray")
	db.variableUnitChange(well, dsLqc, var_gr_max, "gapi")
	db.variableRename(well, dsLqc, var_gr_max, 'GR')
