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
__date__ = """2021-12-09"""
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
for well in db.wellList():
	for ds in db.selectedDatasetList(well):
																																	#Блок гармонизации данных Layers
		for var in db.variableList(well, ds):
			if "KP" in var or "PHIT" in var:
				db.variableFamilyChange(well, ds, var, "Average Porosity")
				if not "td_" in var:
					db.variableRename(well, ds, var, "kpo")
				else:
					db.variableRename(well, ds, var, "td_kpo")
			if "RT" in var:
				db.variableFamilyChange(well, ds, var, "Formation Resistivity Average")
				if not "td_" in var:
					db.variableRename(well, ds, var, "rp")
			if "KRP" in var:
				db.variableFamilyChange(well, ds, var, "Average Permeability")
				if not "td_" in var:
					db.variableRename(well, ds, var, "kpr")
				else:
					db.variableRename(well, ds, var, "td_kpr")
			if "PERM" in var:
				db.variableFamilyChange(well, ds, var, "Average Permeability")
				if not "td_" in var:
					db.variableRename(well, ds, var, "kpr")
				else:
					db.variableRename(well, ds, var, "td_kpr")
			if "KVO" in var or "SXWB" in var:
				db.variableFamilyChange(well, ds, var, "Irreducible Water Saturation")
				db.variableTypeChange(well, ds, var, "TopBottomCurve")
				if not "td_" in var:
					db.variableRename(well, ds, var, "kvo")
				else:
					db.variableRename(well, ds, var, "td_kvo")
			if "SG" in var:
				db.variableFamilyChange(well, ds, var, "Average Hydrocarbon Saturation")
				if not "td_" in var:
					db.variableRename(well, ds, var, "kng")
				else:
					db.variableRename(well, ds, var, "td_kng")
			if "lit" in var:
				db.variableDuplicate(well, ds, var, "td_satur")
				db.variableFamilyChange(well, ds,"td_satur", "Net Pay Flag")
																																				#Блок копирование данных Layers в Rigis_td
		ds_rigis_gm = 'RIGIS_gm'
		ds_rigis_bdntc = 'RIGIS_bdntc'
		ds_rigis_td = 'RIGIS_td'
		ref_name_lay = db.referenceName(well, ds)
		if db.datasetExists(well, ds_rigis_gm):
			print(well, ds, ds_rigis_gm)
			db.datasetDuplicate(well, ds_rigis_gm, well,ds_rigis_td)
			ref_name_td = db.referenceName(well, ds_rigis_td)
			for var in db.variableList(well, ds_rigis_td):
				if var != ref_name_td:
					db.variableDelete(well, ds_rigis_td, var)
			for var in db.variableList(well, ds):
				if var != ref_name_lay:
					db.variableCopy(well, ds, var, ds_rigis_td, var, 'automatic', 'project', 'project', -1, 0, 1)
		else:
			print(well, ds, ds_rigis_bdntc)
			db.datasetDuplicate(well, ds_rigis_bdntc, well,ds_rigis_td)
			ref_name_td = db.referenceName(well, ds_rigis_td)
			for var in db.variableList(well, ds_rigis_td):
				if var != ref_name_td:
					db.variableDelete(well, ds_rigis_td, var)
			for var in db.variableList(well, ds):
				if var != ref_name_lay:
					db.variableCopy(well, ds, var, ds_rigis_td, var, 'automatic', 'project', 'project', -1, 0, 1)
