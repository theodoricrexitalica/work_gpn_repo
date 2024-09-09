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
__date__ = """2022-10-21"""
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
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import win32com.client
import os
import pandas as pd
import re
import datetime
import TechlogDialogAdvanced as tda
dlg = tda.dialogAdvanced("Reports transfer")
dlg.addIntegerInput('report', 'Report qnty', 1, -2147483647, +2147483647, 1, "help")
dlg.execDialog()
num_rep = dlg.getIntegerInput('report')

#Подключаем Outlook через win32com
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")

#Подключаем Outlook через win32com
messages = mapi.Folders("DataStorage").Folders("КонтрольныеСкважины").Items
messages.Sort("[ReceivedTime]", Descending=True)
for msg in list(messages)[:num_rep]:
	attachment = msg.Attachments.Item(1)
	attachment_file = str(msg.Attachments.Item(1))
	report_date = attachment_file.split('_')[2]		
	dt = datetime.datetime.strptime(report_date, '%Y-%m-%d')						#Парсим дату контрольки
	folder_name = dt.strftime('%Y_%b')															#Генерируем папку для отчета месяцу отчета
	print(attachment_file, folder_name)
	path =os.path.join(r'\\10.62.176.27\PetroEngineering_1\Петроинжиниринг\01. ННГ\14. КонтролСкважины Отчеты', 
								folder_name)																#Блок кода для сохранения контрольки сервере
	try:
		os.mkdir(path)																						#Создаем папку с годом и месяцем, если не создана
	except:
		pass
	attachment.SaveASFile(path + '\\' + attachment_file)
