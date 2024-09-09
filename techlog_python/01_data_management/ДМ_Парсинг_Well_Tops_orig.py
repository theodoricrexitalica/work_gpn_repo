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
import os
import TechlogDialogAdvanced as tda
field_list = [	"_vynya",
					"_vyng",
					"_sut",
					"_sug",
					"_situr",
					"_spo",
					"_rom",
					"_zapch",
					"_otd",
					"_nov",
					"_kra",
					"_ety"]

db.currentChange("import")
dlg = tda.dialogAdvanced("Загрузка месторождения")
input_fld = dlg.addListInput("field_list", "Месторождения", field_list, 0, 1, "help")
dlg.execDialog()
output_fld = dlg.getListInput("field_list")


#tempFolder = "E:\\OilFields\\Еты-Пуровское\\A2\\zones\\"
#tempFile = os.path.join(tempFolder , "Well_Tops")
tempFile = rtc.getOpenFileName("Well Tops", multiselect = True, filter = ["All files;*.*"])

wells_txt = [] 
data_txt = []
with open(tempFile[0], "r", -1, "ansi") as file:
    for line in file.readlines()[13:]:
    	line = line.replace("\n", " ")
    	if not "_K" in line:
    		if not "_BOT" in line:
    			well_name = ((line.split(" ")[7]).replace("\"", ""))
		    	wells_txt.append(well_name)
		    	data_txt.append(line.split(" ")[6] + ";" + line.split(" ")[4])
print(wells_txt)
db.currentChange("import")

for i in range(len(wells_txt)):
	db.wellCreate(wells_txt[i])
for well in db.wellList():
	list_md = []
	list_zones = []
	for i in range(len(wells_txt)):
		if well == wells_txt[i]:
			try:
				list_md.append(float(data_txt[i].split(";")[1]))
				list_zones.append((data_txt[i].split(";")[0]).replace("\"", ""))
			except:
				list_md.append(0)
				list_zones.append(" ")
	db.datasetCreate(well, "ZONES" + output_fld, "MD", "Measured Depth", "m", list_md, "double")
	db.datasetTypeChange(well, "ZONES" + output_fld, "interval")
	db.variableSave(well, "ZONES" + output_fld, "ZONES", "Zone Name", "unitless", list_zones, 0, "auto")
