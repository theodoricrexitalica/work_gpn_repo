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
__date__ = """2023-03-27"""
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
import datetime as dt
import TechlogDialogAdvanced as tda
import pytz

oilfieldsCodes = {'036':'ЕТЫ-ПУРОВСКОЕ','092':'РОМАНОВСКОЕ','120':'СПОРЫШЕВСКОЕ','237':'МУРАВЛЕНКОВСКОЕ',
							'254':'СУТОРМИНСКОЕ','256':'КРАЙНЕЕ'}

local_tz = pytz.timezone('Europe/Moscow')
today = dt.datetime.today().replace(tzinfo=pytz.utc).astimezone(local_tz)
dd = dt.timedelta(days=60)
minus_month = today - dd
print(today.strftime('%d-%m-%Y'), '-', minus_month.strftime('%d-%m-%Y'))
print()

outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
messages = mapi.Folders("DataStorage").Folders("Новые скважины в БД").Items
messages.Sort("[ReceivedTime]", Descending=True)

wellListRigis = []
for msg in list(messages)[:]:
	msg_date = (msg.ReceivedTime)
	if msg_date > minus_month:
		well_num = (msg.Body.split('\t\r\n')[1]).split('\t')[0]
		body = msg.Body
		numbers = re.findall('[0-9]+_[0-9GPLd]+', body)
		#print(numbers, msg_date.strftime('%d.%m.%y'))
		for item in numbers:
			wellListRigis.append(item)
wellListRigis = list(set(wellListRigis))
wellListRigis = sorted(wellListRigis)
for nameWell in wellListRigis:
	for key in oilfieldsCodes.keys():
		if nameWell.split('_')[0] == key:
			print(oilfieldsCodes[key], '-', nameWell.split('_')[1])
