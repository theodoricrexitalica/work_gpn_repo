# -*- coding: utf-8 -*-
from __future__ import division
#Declarations
#The dictionary of parameters
#name,bname,type,family,unit,value,mode,description,group,min,max,list,enable,iscombocheckbox,isused
parameterDict = {}
try:
	if Parameter:
		pass
except NameError:
	class Parameter:
		def __init__(self, **d):
			pass
#DeclarationsEnd
import os
import sys
sys.path.append("C:\Apps\Routine\PP_eval\pypyodbc-1.3.1\\")
import pypyodbc

myconnection = pypyodbc.connect("DSN=EDM_UI_PRODUCTION;UID=SPDIQM;PWD=SPDIQM") 
mycursor = myconnection.cursor()

def GET_WELL_NAME(well):
	well=well.replace("_", "-")

	wellname_arr=well.split('-')
	wellnum=wellname_arr[1]
	if wellnum[0]=="0":
		wellnum=wellnum[1:]
	wellname=wellname_arr[0]+'-'+wellnum
	return wellname

def GET_WELL_ID(well):


	sql="select A.WELL_ID from EDM.cd_well a, cd_site s  where  a.site_id = s.site_id AND  s.project_id in ('uepgCCUr88','zubFM70aiT','iZGXXF4Sq8')  AND A.WELL_COMMON_NAME like '" + str(well) + "%'"
	mycursor.execute(sql)
	WELL_ID_result=""
	for WELL_ID  in mycursor.fetchall():
		if not WELL_ID==None:
			WELL_ID_result=WELL_ID[0]
	if  WELL_ID_result=="":
		print("error: не найдена  скважина "+str(WELL_ID)+"\n")
	return WELL_ID_result

def GET_WELLBORE_ID(well):

	sql="select R.WELLBORE_ID from dm_pipe_run r, dm_pipe_tally p, cd_well w, cd_site s where w.site_id = s.site_id and w.well_id = p.well_id and r.well_id= p.well_id and p.PIPE_RUN_ID = r.PIPE_RUN_ID and s.project_id in ('uepgCCUr88','zubFM70aiT','iZGXXF4Sq8') and run_tally_type = 'RUN' and round(total_length*0.3048,0)>2000 AND  w.WELL_COMMON_NAME like '" + str(well) + "%'"
	mycursor.execute(sql)
	WELLBORE_ID_result=""
	for WELLBORE_ID  in mycursor.fetchall():
		if not WELLBORE_ID==None:
			WELLBORE_ID_result=WELLBORE_ID[0]
	if  WELLBORE_ID_result=="":
		print("error: не найден ствол "+str(WELLBORE_ID)+"\n")
	return WELLBORE_ID_result

def GET_EVENT_ID(well):

	sql="select R.EVENT_ID from dm_pipe_run r, dm_pipe_tally p, cd_well w, cd_site s where w.site_id = s.site_id and w.well_id = p.well_id and r.well_id= p.well_id and p.PIPE_RUN_ID = r.PIPE_RUN_ID and s.project_id in ('uepgCCUr88','zubFM70aiT','iZGXXF4Sq8') and run_tally_type = 'RUN' and round(total_length*0.3048,0)>2000 AND  w.WELL_COMMON_NAME like '" + str(well) + "%'"
	mycursor.execute(sql)
	EVENT_ID_result=""
	for EVENT_ID  in mycursor.fetchall():
		if not EVENT_ID==None:
			EVENT_ID_result=EVENT_ID[0]
	if  EVENT_ID_result=="":
		print("error: не найден EVENT_ID для "+str(well)+"\n")
	return EVENT_ID_result

def GET_REPORT_JOURNAL_ID(well_id, date_report):

	sql="SELECT A.REPORT_JOURNAL_ID FROM EDM.DM_REPORT_JOURNAL a WHERE A.WELL_ID='"+str(well_id)+"' AND CREATE_USER_ID='Techlog upload' AND DATE_REPORT=TO_DATE('"+str(date_report)+"', 'dd/mm/yyyy')+3"
	#print sql
	mycursor.execute(sql)
	REPORT_JOURNAL_ID_result=""
	for REPORT_JOURNAL_ID  in mycursor.fetchall():
		if not REPORT_JOURNAL_ID==None:
			REPORT_JOURNAL_ID_result=REPORT_JOURNAL_ID[0]
	if  REPORT_JOURNAL_ID_result=="":
		print("error: не найден REPORT_JOURNAL_ID для "+str(well)+"\n")
	return REPORT_JOURNAL_ID_result

def GET_PIPE_RUN_ID(well_id, date_report, report_journal_id):
	sql="SELECT PIPE_RUN_ID FROM EDM.DM_PIPE_RUN a WHERE A.WELL_ID='"+str(well_id)+"' AND DATE_REPORT=TO_DATE('"+str(date_report)+"', 'dd/mm/yyyy')+3 AND REPORT_JOURNAL_ID='" +str(report_journal_id)+ "'"
	#print sql
	mycursor.execute(sql)
	PIPE_RUN_ID_result=""
	for PIPE_RUN_ID  in mycursor.fetchall():
		if not PIPE_RUN_ID==None:
			PIPE_RUN_ID_result=PIPE_RUN_ID[0]
	if  PIPE_RUN_ID_result=="":
		print("error: не найден RPIPE_RUN_ID для "+str(well_id)+"\n")
	return PIPE_RUN_ID_result

def GET_DATE_REPORT(well):
	sql="select max(DATE_REPORT) as DATE_REPORT  from dm_pipe_run r, dm_pipe_tally p, cd_well w, cd_site s where w.site_id = s.site_id and w.well_id = p.well_id and r.well_id= p.well_id and p.PIPE_RUN_ID = r.PIPE_RUN_ID and s.project_id in ('uepgCCUr88','zubFM70aiT','iZGXXF4Sq8') and run_tally_type = 'RUN' and round(total_length*0.3048,0)>2000 AND  w.WELL_COMMON_NAME like '" + str(well) + "%'"
	mycursor.execute(sql)
	DATE_REPORT_result=""
	for DATE_REPORT  in mycursor.fetchall():
		if not DATE_REPORT==None:
			DATE_REPORT_result=DATE_REPORT[0]
	if  DATE_REPORT_result=="":
		print("error: не найден ствол "+str(DATE_REPORT)+"\n")
	return DATE_REPORT_result

def REMOVE_CASING_COLLAR_FROM_EDM(well_id):
	sql="select distinct REPORT_JOURNAL_ID from DM_REPORT_JOURNAL WHERE WELL_ID='"+well_id+"' AND CREATE_USER_ID='Techlog upload'"
	mycursor.execute(sql)
	REPORT_JOURNAL_ID_result=""
	for REPORT_JOURNAL_ID  in mycursor.fetchall():
		REPORT_JOURNAL_ID_result=REPORT_JOURNAL_ID[0]

	sql="select distinct PIPE_RUN_ID from DM_PIPE_RUN WHERE WELL_ID='"+well_id+"' AND REPORT_JOURNAL_ID='"+REPORT_JOURNAL_ID_result+"'"
	mycursor.execute(sql)
	PIPE_RUN_ID_result=""
	for PIPE_RUN_ID  in mycursor.fetchall():
		PIPE_RUN_ID_result=PIPE_RUN_ID[0]

	sql="DELETE FROM  DM_PIPE_TALLY WHERE  PIPE_RUN_ID='"+PIPE_RUN_ID_result+"' AND  WELL_ID='"+well_id+"'"
	#print sql
	mycursor.execute(sql)
	mycursor.execute("commit")

	sql="DELETE FROM  DM_PIPE_RUN WHERE  PIPE_RUN_ID='"+PIPE_RUN_ID_result+"' AND  WELL_ID='"+well_id+"'"
	#print sql
	mycursor.execute(sql)
	mycursor.execute("commit")
	
	sql="DELETE FROM DM_REPORT_JOURNAL WHERE  REPORT_JOURNAL_ID='"+REPORT_JOURNAL_ID_result+"' AND  WELL_ID='"+well_id+"'"
	#print sql
	mycursor.execute(sql)
	mycursor.execute("commit")
	return "1"

__author__ = """Taras DOLGUSHIN (dolgushin.tyu)"""
__date__ = """2022-12-07"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""