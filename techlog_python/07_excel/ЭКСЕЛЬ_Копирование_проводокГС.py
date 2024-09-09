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
__date__ = """2022-11-29"""
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
import datetime as dt

last_week = dt.date.today()- dt.timedelta(days = 7)
last_week = last_week.strftime('%m/%d/%Y %H:%M %p')

#Подключаем Outlook через win32com
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")

messages = mapi.Folders("DataStorage").Folders("ЦУСС").Items
messages = messages.Restrict("[ReceivedTime] >= '" + last_week + "'")
messages.Sort("[ReceivedTime]", Descending=True)

for msg in list(messages):
	subj_msg = msg.Subject
	if 'стоп' in subj_msg.lower():
		attachment = msg.Attachments.Item(1)
		attachment_file = str(msg.Attachments.Item(1))
		#print(subj_msg)
		print(attachment_file)
		if 'вынгапур' in subj_msg.lower():
			folder_name = 'Вынгапуровское'
		#if len(attachment_file.split('_')[5]) < 4:
			#folder_name = attachment_file.split('_')[6]
		#else:
			#folder_name = attachment_file.split('_')[5]
			path =os.path.join(r'\\10.62.176.27\PetroEngineering_1\Личные папки\Долгушин', folder_name)
			try:
				os.mkdir(path)
			except:
				pass
			attachment.SaveASFile(path + '\\' + attachment_file)
os.startfile(path)
