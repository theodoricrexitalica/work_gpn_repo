select *
from rdfsmart_ods.mer_v mv 
inner join (select w.oil_field, w.well, w.objectname 
			from rdfsmart_ods.wellcluster w where 
			w.oil_field like 'Восточно-Пякутинское' 
			and w.objectname like 'КУСТ-4') w on mv.wellbore = w.well 
where 
mv.oil_field like 'Восточно-Пякутинское'


--Поиск скважин, кустов, месторождений
select well_id, well_name, well_cluster, field_id, field_name
from wellop_ods.v_well_full
where field_name like 'Восточно-Пякутинское' and well_cluster = '4'


--explain analyze
with all_dates as (
SELECT date_trunc('day', dd):: date as dt
FROM generate_series
        ('2014-01-01'::timestamp 
        ,'2023-05-05'::timestamp
        , '1 day'::interval) dd),
all_date_well as (
select ad.dt, F.sk_1 
from all_dates ad
join ois_ods.fond F on F.xr_1 = 'XR0011' and F.dwh_is_active=true and F.SK_1 in (
					2550601200, 2550778100, 2550601000, 2550777900, 2550601400, 2550777700, 2550777800,
					2550000212, 2550601500, 2550000199, 2550778000, 2550601300, 2550601600, 2550601100) 
and ad.dt between to_timestamp(cast(F.dz_1 as varchar), 'yyyymmdd')+(cast(F.tz_1 as varchar)||(' minutes'))::interval 
and to_timestamp(REPLACE(cast (F.D2_1 as varchar), '99999999', '20990101'),'yyyymmdd')+(cast(F.t2_1 as varchar)||(' minutes'))::interval 
join ois_ods.spskv sk on F.SK_1 = sk.sk_1
where sk.ms_1= 'MS0255')
select *
from (select SKV.SK_1 as "Well_ID",
			(SELECT NE_1 FROM ois_ods.class WHERE CD_1 = SKV.MS_1) AS "Месторождение",
             date(adw.dt) AS "Дата",
             SKV.S1_1 AS "Скважина",                                    
             (select concat(cast(SKV.KS_1 as varchar),SKV.lk_1)) as "Куст",
             (SELECT NE_1 FROM ois_ods.class WHERE CD_1 = F.XR_1) as "Характер работы",                   
             (SELECT NE_1 FROM ois_ods.class WHERE CD_1 ='SS'||TO_CHAR(min(cast(replace(SO.SS_1,'SS','') as integer)), 'fm0000')) AS "Состояние",   
              string_agg(distinct ((select ne_1 from ois_ods.class where cd_1 = r.pl_1)),';') as "Пласт", 
              string_agg(distinct cast(cast(ud.pk_1 as integer) as varchar),';' ) as "Пластовое P кровля [атм]",                                 
              max( case when MT.SHORT_NAME='Qж ТМ' then WM.VALUE else cast(null as float) end ) "Qж  (ТМ) [м3/сут]",
              max( case when MT.SHORT_NAME='Qж' then WM.VALUE else cast(null as float) end ) "Qж ручной [м3/сут]",             
              max( case when MT.SHORT_NAME='Qн ТМ' then WM.VALUE else cast(null as float) end ) "Qн (ТМ) [тн/сут]",
              max( case when MT.SHORT_NAME='Qн' then WM.VALUE else cast(null as float) end ) "Qн расчёт [тн/сут]",  
              max( case when MT.SHORT_NAME='Обв ТМ' then WM.VALUE else cast(null as float) end ) "Обв-ть V (ТМ) [%]",
              max( case when MT.SHORT_NAME='Обв ХАЛ' then WM.VALUE else cast(null as float) end ) "Обв-ть V (ХАЛ) [%]",
              max( case when MT.SHORT_NAME='Обв' and WM.confirmed=1 then WM.VALUE else cast(null as float) end ) "Обв-ть V ручная [%]",             
              max( case when MT.SHORT_NAME='Qгаз ТМ' then WM.VALUE else cast(null as float) end ) "Qг (ТМ) [м3/сут]",
              max( case when MT.SHORT_NAME='ГФР(ТМ)' then WM.VALUE else cast(null as float) end ) "ГФ (расч. ТМ) [м3/тн]",
              round(max( case when MT.SHORT_NAME='Pзаб(Hд)' then WM.VALUE else cast(null as integer) end ),1) "Pзаб от Hд",
              round(max( case when MT.SHORT_NAME='Pзаб(Pпр)' then WM.VALUE else cast(null as integer) end ),1) "Pзаб от Pпр",  
              max( case when MT.SHORT_NAME='Pзаб (иссл.)' and WM.confirmed=1 then WM.VALUE else cast(null as float) end ) "Pзаб по исследованию"
-- Виртуальная табличка – порядок дат             
      		  FROM all_date_well adw
-- Замеры ТМ и ручные      
     		  inner join wellop_ods.well_measure WM on date(WM.MEASURE_DATE)=date(adw.dt) and WM.WELL_ID=adw.sk_1 and WM.dwh_is_active=true 
      		  and WM.MEASURE_TYPE_ID in (30, 204, 1103, 1104, 33, 4, 3, 1, 11, 12, 7026, 7005)
--      		  and WM.well_id in (
--      	110076600,	110058800,	110050000,	110169000,	110001500,	110020500,	110053800,	110074600,	110304800,	110302100,	
--		110143900,	110150700,	110047600,	110043100,	110038200,	110043800,	110042000,	110044600,	110050100,	110050800,	
--		110060000,	110068200,	110028900,	110127900,	110115700,	110141000,	110143800,	110159500,	110159600,	110016500,	
--		110305600,	110129900,	110062100,	110035200,	110070900,	110015700,	110018600,	110038600,	110110200,	110166100,	
--		110066200,	110035300,	110062900,	110063300,	110138200,	110150900,	110061800,	110047000,	110044700,	110050400,	
--		110061900,	110029800,	110030100,	110030500,	110113400,	110150300,	110529000,	110306200,	110401100,	110063100,	
--		110059200,	110303500,	110304500,	110130700,	110030700,	110001300,	110004609,	110047700,	110054000,	110032500,	
--		110147100,	110160000,	110169100)
-- Расшифровка вида замера      
              left join wellop_ods.measure_type MT on WM.MEASURE_TYPE_ID = MT.ID and MT.dwh_is_active=true
-- Состояние      
     		  inner join ois_ods.sost SO on SO.SK_1 = adw.sk_1 
--              and SO.sk_1 in (
--        110076600,	110058800,	110050000,	110169000,	110001500,	110020500,	110053800,	110074600,	110304800,	110302100,	
--		110143900,	110150700,	110047600,	110043100,	110038200,	110043800,	110042000,	110044600,	110050100,	110050800,	
--		110060000,	110068200,	110028900,	110127900,	110115700,	110141000,	110143800,	110159500,	110159600,	110016500,	
--		110305600,	110129900,	110062100,	110035200,	110070900,	110015700,	110018600,	110038600,	110110200,	110166100,	
--		110066200,	110035300,	110062900,	110063300,	110138200,	110150900,	110061800,	110047000,	110044700,	110050400,	
--		110061900,	110029800,	110030100,	110030500,	110113400,	110150300,	110529000,	110306200,	110401100,	110063100,	
--		110059200,	110303500,	110304500,	110130700,	110030700,	110001300,	110004609,	110047700,	110054000,	110032500,	
--		110147100,	110160000,	110169100) 
              and (case when WM.MEASURE_DATE is null then adw.dt else WM.MEASURE_DATE end) 
              between to_timestamp(cast(SO.dz_1 as varchar), 'yyyymmdd')+(cast((SO.tz_1) as varchar)||(' minutes'))::interval 
              and to_timestamp(REPLACE(cast (SO.D2_1 as varchar), '99999999', '20990101'),'yyyymmdd')+(cast(SO.t2_1 as varchar)||(' minutes'))::interval 
              and SO.dwh_is_active=true                                    
-- Характер работы
      inner join ois_ods.fond F on F.SK_1 = adw.sk_1 and F.xr_1 = 'XR0011' and F.dwh_is_active=true  
--              and F.sk_1 in (
--        110076600,	110058800,	110050000,	110169000,	110001500,	110020500,	110053800,	110074600,	110304800,	110302100,	
--		110143900,	110150700,	110047600,	110043100,	110038200,	110043800,	110042000,	110044600,	110050100,	110050800,	
--		110060000,	110068200,	110028900,	110127900,	110115700,	110141000,	110143800,	110159500,	110159600,	110016500,	
--		110305600,	110129900,	110062100,	110035200,	110070900,	110015700,	110018600,	110038600,	110110200,	110166100,	
--		110066200,	110035300,	110062900,	110063300,	110138200,	110150900,	110061800,	110047000,	110044700,	110050400,	
--		110061900,	110029800,	110030100,	110030500,	110113400,	110150300,	110529000,	110306200,	110401100,	110063100,	
--		110059200,	110303500,	110304500,	110130700,	110030700,	110001300,	110004609,	110047700,	110054000,	110032500,	
--		110147100,	110160000,	110169100)
-- Общая информация по скважине (административная), привязки                                   
      inner join ois_ods.spskv SKV on adw.sk_1 = SKV.SK_1 and SKV.dwh_is_active=true                
 -- Дебит OIS протянутые                       
      inner join ois_ods.zam z on WM.WELL_ID = Z.SK_1 and Z.dwh_is_active=true  
      and adw.dt >= z.dwh_begin_date and adw.dt <  COALESCE(z.dwh_end_date,to_timestamp('20990101','yyyymmdd')) - interval '1 sec'              
-- Название пласта протянутое test                
      inner join ois_ods.rabpl r on wm.well_id = r.sk_1 and r.dwh_is_active=true 
      and adw.dt >= r.dwh_begin_date and adw.dt < COALESCE(r.dwh_end_date,to_timestamp('20990101','yyyymmdd')) - interval '1 sec'                                                                         
-- Пластовое давление OIS протянутое test                         
      inner join ois_ods.udapl ud on wm.well_id = ud.sk_1 and ud.dwh_is_active=true and r.pl_1=ud.pl_1
      and adw.dt>=ud.dwh_begin_date and adw.dt<COALESCE(ud.dwh_end_date,to_timestamp('20990101','yyyymmdd')) - interval '1 sec'    
 	  where WM.MEASURE_TYPE_ID in (30, 204, 1103, 1104, 33, 4, 3, 1, 11, 12, 7026, 7005)
	  group by SKV.S1_1,SKV.SK_1,  SKV.MS_1, SKV.lk_1, SKV.gu_1, SKV.om_1, SKV.pr_1, SKV.zx_1, SKV.st2_1, 
	  SKV.dn_1, SKV.db_1, SKV.pp_1, SKV.c1_1, date(adw.dt), SKV.KS_1, F.XR_1       
) t