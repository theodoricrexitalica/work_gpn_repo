with all_dates as (
SELECT date_trunc('day', dd):: date as dt
FROM generate_series
        ('2014-01-01'::timestamp 
        ,'2023-04-01'::timestamp
        , '1 day'::interval) dd),
all_date_well as (        
select ad.dt, F.sk_1 from all_dates ad
join ois_ods.fond F on F.xr_1 = 'XR0011' and F.dwh_is_active=true and (F.sk_1 > 110000000 and F.sk_1 < 119999999) and
 F.SK_1 in 
		(
		110110200, 110113200, 110113400, 110115700, 110001200, 110127900, 110129900, 110001300, 110130700, 110013800, 
		110138100, 110138200, 110001400, 110141000, 110143800, 110143900, 110147100, 110148000, 110001500, 110150300,
		110150700, 110150900, 110015700, 110159500, 110159600, 110160000, 110016200, 110016500, 110016600, 110166100, 
		110169000, 110169100, 110173900, 110018100, 110018600, 110019200, 110019400, 110020500, 110020600, 110023700,
		110024300, 110024700, 110024900, 110025000, 110028900, 110029800, 110000204, 110030100, 110302100, 110303500, 
		110304500, 110304800, 110030500, 110305600, 110305700, 110306200, 110030700, 110032100, 110032500, 110003400,
		110035200, 110035300, 110035600, 110036000, 110038200, 110038400, 110038600, 110401000, 110401100, 110411000, 
		110042000, 110422500, 110422700, 110427800, 110043100, 110043800, 110044400, 110044600, 110044700, 110004609,
		110047000, 110047200, 110047600, 110047700, 110050000, 110050100, 110502600, 110050400, 110050700, 110050800, 
		110051000, 110529000, 110053800, 110054000, 110054100, 110058800, 110059200, 110060000, 110061800, 110061900,
		110062000, 110062100, 110621400, 110062900, 110063100, 110631700, 110063300, 110065500, 110066200, 110680700, 
		110068200, 110683000, 110070900, 110007400, 110074600, 110076600, 110077600, 110803100, 110805200, 110807000
		) and ad.dt between to_timestamp(cast(F.dz_1 as varchar), 'yyyymmdd')+(cast(F.tz_1 as varchar)||(' minutes'))::interval 
          and to_timestamp(REPLACE(cast (F.D2_1 as varchar), '99999999', '20990101'),'yyyymmdd')+(cast(F.t2_1 as varchar)||(' minutes'))::interval 
join ois_ods.spskv sk on F.SK_1 = sk.sk_1 and (sk.sk_1 > 110000000 and sk.sk_1 < 119999999)
where (sk.ms_1= 'MS0011')
--where (sk.ms_1= 'MS0849') or (sk.ms_1='MS0640')
)
Select *
FROM (SELECT 
             SKV.SK_1 as "Well_ID",
			(SELECT NE_1 FROM ois_ods.class WHERE CD_1 = SKV.MS_1) AS "Месторождение",
             date(adw.dt) AS "Дата",
             SKV.S1_1 AS "Скважина",                                    
             (select concat(cast(SKV.KS_1 as varchar),SKV.lk_1)) as "Куст",
  
--             (select ne_1 from ois_ods.class where SKV.om_1=cd_1) as "ДО",
-- 
--             (select ne_1 from ois_ods.class where SKV.zx_1=cd_1) as "Кластер",
--             (select ne_1 from ois_ods.class where SKV.st2_1=cd_1) as "Участок",                               
--             (select ne_1 from ois_ods.class where SKV.c1_1=cd_1) as "Тип ствола",
                                    (SELECT NE_1 FROM ois_ods.class WHERE CD_1 = F.XR_1) as "Характер работы",                   
                  (SELECT NE_1 FROM ois_ods.class WHERE CD_1 ='SS'||TO_CHAR(min(cast(replace(SO.SS_1,'SS','') as integer)), 'fm0000')) AS "Состояние",   
--              (count(distinct r.pl_1)) as "Количество пластов",
--              string_agg(distinct (select ne_1 from ois_ods.class where cd_1 = r.pl_1)||'-'||cast(round(cast(skpl.pn_1 as integer),1) as varchar),';') as "Пласт-Распределение по пластам",  
              string_agg(distinct ((select ne_1 from ois_ods.class where cd_1 = r.pl_1)),';') as "Пласт", 
--              string_agg(distinct cast(round(cast(skpl.pn_1 as integer),1) as varchar),';') as "Распределение по пластам",
              string_agg(distinct cast(cast(ud.pk_1 as integer) as varchar),';' ) as "Пластовое P кровля [атм]",             
          
                   
 --            max( case when MT.SHORT_NAME='Tраб(ОИС)' then WM.VALUE else cast(null as float) end ) "Время работы (ОИС)",                       
              max( case when MT.SHORT_NAME='Qж ТМ' then WM.VALUE else cast(null as float) end ) "Qж  (ТМ) [м3/сут]",
              max( case when MT.SHORT_NAME='Qж' then WM.VALUE else cast(null as float) end ) "Qж ручной [м3/сут]",             
--              case when min(cast(replace(SO.SS_1,'SS','') as integer))=1 then max( z.qj_1 ) else cast(null as float) end as "Qж OIS протяжка [м3/сут]", 
                   
              max( case when MT.SHORT_NAME='Qн ТМ' then WM.VALUE else cast(null as float) end ) "Qн (ТМ) [тн/сут]",
              max( case when MT.SHORT_NAME='Qн' then WM.VALUE else cast(null as float) end ) "Qн расчёт [тн/сут]",  
--              case when min(cast(replace(SO.SS_1,'SS','') as integer))=1 then max( z.qn_1 ) else cast(null as float) end as "Qн OIS протяжка [тн/сут]",           

                   
              max( case when MT.SHORT_NAME='Обв ТМ' then WM.VALUE else cast(null as float) end ) "Обв-ть V (ТМ) [%]",
              max( case when MT.SHORT_NAME='Обв ХАЛ' then WM.VALUE else cast(null as float) end ) "Обв-ть V (ХАЛ) [%]",
              max( case when MT.SHORT_NAME='Обв' and WM.confirmed=1 then WM.VALUE else cast(null as float) end ) "Обв-ть V ручная [%]",             
--              case when min(cast(replace(SO.SS_1,'SS','') as integer))=1 then max( z.so_1 ) else cast(null as float) end as "Обв-ть V OIS протяжка [%]", 
              max( case when MT.SHORT_NAME='Qгаз ТМ' then WM.VALUE else cast(null as float) end ) "Qг (ТМ) [м3/сут]",
                  -- 0 as "GOR FREE",
              max( case when MT.SHORT_NAME='ГФР(ТМ)' then WM.VALUE else cast(null as float) end ) "ГФ (расч. ТМ) [м3/тн]",

                   
              round(max( case when MT.SHORT_NAME='Pзаб(Hд)' then WM.VALUE else cast(null as integer) end ),1) "Pзаб от Hд",
              round(max( case when MT.SHORT_NAME='Pзаб(Pпр)' then WM.VALUE else cast(null as integer) end ),1) "Pзаб от Pпр",  
              max( case when MT.SHORT_NAME='Pзаб (иссл.)' and WM.confirmed=1 then WM.VALUE else cast(null as float) end ) "Pзаб по исследованию"
                   
-- Виртуальная табличка – порядок дат             
      FROM all_date_well adw

-- Замеры ТМ и ручные      
      left join wellop_ods.well_measure WM on date(WM.MEASURE_DATE)=date(adw.dt) and WM.WELL_ID=adw.sk_1 and WM.dwh_is_active=true and (WM.well_id > 110000000 and WM.well_id < 119999999) and WM.MEASURE_TYPE_ID in (30, 204, 1103, 1104, 33, 4, 3, 1, 11, 12, 7026, 7005)
		and Wm.well_id in (
		110110200, 110113200, 110113400, 110115700, 110001200, 110127900, 110129900, 110001300, 110130700, 110013800, 
		110138100, 110138200, 110001400, 110141000, 110143800, 110143900, 110147100, 110148000, 110001500, 110150300,
		110150700, 110150900, 110015700, 110159500, 110159600, 110160000, 110016200, 110016500, 110016600, 110166100, 
		110169000, 110169100, 110173900, 110018100, 110018600, 110019200, 110019400, 110020500, 110020600, 110023700,
		110024300, 110024700, 110024900, 110025000, 110028900, 110029800, 110000204, 110030100, 110302100, 110303500, 
		110304500, 110304800, 110030500, 110305600, 110305700, 110306200, 110030700, 110032100, 110032500, 110003400,
		110035200, 110035300, 110035600, 110036000, 110038200, 110038400, 110038600, 110401000, 110401100, 110411000, 
		110042000, 110422500, 110422700, 110427800, 110043100, 110043800, 110044400, 110044600, 110044700, 110004609,
		110047000, 110047200, 110047600, 110047700, 110050000, 110050100, 110502600, 110050400, 110050700, 110050800, 
		110051000, 110529000, 110053800, 110054000, 110054100, 110058800, 110059200, 110060000, 110061800, 110061900,
		110062000, 110062100, 110621400, 110062900, 110063100, 110631700, 110063300, 110065500, 110066200, 110680700, 
		110068200, 110683000, 110070900, 110007400, 110074600, 110076600, 110077600, 110803100, 110805200, 110807000
		)
-- Расшифровка вида замера      
      left join wellop_ods.measure_type MT on WM.MEASURE_TYPE_ID = MT.ID and MT.dwh_is_active=true

-- Состояние      
      left join ois_ods.sost SO on SO.SK_1 = adw.sk_1 and (so.sk_1 > 110000000 and so.sk_1 < 119999999)
      and SO.sk_1 in (
		110110200, 110113200, 110113400, 110115700, 110001200, 110127900, 110129900, 110001300, 110130700, 110013800, 
		110138100, 110138200, 110001400, 110141000, 110143800, 110143900, 110147100, 110148000, 110001500, 110150300,
		110150700, 110150900, 110015700, 110159500, 110159600, 110160000, 110016200, 110016500, 110016600, 110166100, 
		110169000, 110169100, 110173900, 110018100, 110018600, 110019200, 110019400, 110020500, 110020600, 110023700,
		110024300, 110024700, 110024900, 110025000, 110028900, 110029800, 110000204, 110030100, 110302100, 110303500, 
		110304500, 110304800, 110030500, 110305600, 110305700, 110306200, 110030700, 110032100, 110032500, 110003400,
		110035200, 110035300, 110035600, 110036000, 110038200, 110038400, 110038600, 110401000, 110401100, 110411000, 
		110042000, 110422500, 110422700, 110427800, 110043100, 110043800, 110044400, 110044600, 110044700, 110004609,
		110047000, 110047200, 110047600, 110047700, 110050000, 110050100, 110502600, 110050400, 110050700, 110050800, 
		110051000, 110529000, 110053800, 110054000, 110054100, 110058800, 110059200, 110060000, 110061800, 110061900,
		110062000, 110062100, 110621400, 110062900, 110063100, 110631700, 110063300, 110065500, 110066200, 110680700, 
		110068200, 110683000, 110070900, 110007400, 110074600, 110076600, 110077600, 110803100, 110805200, 110807000
		)
                                  AND (case when WM.MEASURE_DATE is null then adw.dt else WM.MEASURE_DATE end) between to_timestamp(cast(SO.dz_1 as varchar), 'yyyymmdd')+(cast((SO.tz_1) as varchar)||(' minutes'))::interval 
                                          and to_timestamp(REPLACE(cast (SO.D2_1 as varchar), '99999999', '20990101'),'yyyymmdd')+(cast(SO.t2_1 as varchar)||(' minutes'))::interval 
                                          and SO.dwh_is_active=true                                  
      
-- Характер работы
      left join ois_ods.fond F on F.SK_1 = adw.sk_1 and (F.xr_1 = 'XR0011') and (F.sk_1 > 110000000 and F.sk_1 < 119999999) -- ХАРАКТЕР НАГНЕТАТЕЛЬНАЯ 
                                  and F.dwh_is_active=true  
                                        and F.sk_1 in (
		110110200, 110113200, 110113400, 110115700, 110001200, 110127900, 110129900, 110001300, 110130700, 110013800, 
		110138100, 110138200, 110001400, 110141000, 110143800, 110143900, 110147100, 110148000, 110001500, 110150300,
		110150700, 110150900, 110015700, 110159500, 110159600, 110160000, 110016200, 110016500, 110016600, 110166100, 
		110169000, 110169100, 110173900, 110018100, 110018600, 110019200, 110019400, 110020500, 110020600, 110023700,
		110024300, 110024700, 110024900, 110025000, 110028900, 110029800, 110000204, 110030100, 110302100, 110303500, 
		110304500, 110304800, 110030500, 110305600, 110305700, 110306200, 110030700, 110032100, 110032500, 110003400,
		110035200, 110035300, 110035600, 110036000, 110038200, 110038400, 110038600, 110401000, 110401100, 110411000, 
		110042000, 110422500, 110422700, 110427800, 110043100, 110043800, 110044400, 110044600, 110044700, 110004609,
		110047000, 110047200, 110047600, 110047700, 110050000, 110050100, 110502600, 110050400, 110050700, 110050800, 
		110051000, 110529000, 110053800, 110054000, 110054100, 110058800, 110059200, 110060000, 110061800, 110061900,
		110062000, 110062100, 110621400, 110062900, 110063100, 110631700, 110063300, 110065500, 110066200, 110680700, 
		110068200, 110683000, 110070900, 110007400, 110074600, 110076600, 110077600, 110803100, 110805200, 110807000
		)

-- Общая информация по скважине (административная), привязки                                   
      left join ois_ods.spskv SKV on adw.sk_1 = SKV.SK_1 and SKV.dwh_is_active=true and (skv.sk_1 > 110000000 and skv.sk_1 < 119999999)
   
               
 -- Дебит OIS протянутые                       
      left join ois_ods.zam z on WM.WELL_ID = Z.SK_1 and Z.dwh_is_active=true and  (z.sk_1 > 110000000 and z.sk_1 < 119999999) and
      
                              adw.dt >= z.dwh_begin_date and adw.dt <  COALESCE(z.dwh_end_date,to_timestamp('20990101','yyyymmdd')) - interval '1 sec'  
                              
                                                          
-- Название пласта протянутое test                
      left join ois_ods.rabpl r on wm.well_id = r.sk_1 and r.dwh_is_active=true and  (r.sk_1 > 110000000 and r.sk_1 < 119999999) and
                                     adw.dt >= r.dwh_begin_date and adw.dt < COALESCE(r.dwh_end_date,to_timestamp('20990101','yyyymmdd')) - interval '1 sec'        
                                                                                                              
-- Пластовое давление OIS протянутое test                         
      left join ois_ods.udapl ud on wm.well_id = ud.sk_1 and ud.dwh_is_active=true and r.pl_1=ud.pl_1 and (r.sk_1 > 110000000 and r.sk_1 < 119999999) and
                                     adw.dt>=ud.dwh_begin_date and adw.dt<COALESCE(ud.dwh_end_date,to_timestamp('20990101','yyyymmdd')) - interval '1 sec'                                            
                                          
-- Буферное, затрубное, линейное давления OIS протянутые test                         
--      left join ois_ods.udav u on wm.well_id = u.sk_1 and u.dwh_is_active=true and (u.sk_1 > 110000000 and u.sk_1 < 119999999) and 
--                                     adw.dt>= u.dwh_begin_date and adw.dt<COALESCE(u.dwh_end_date,to_timestamp('20990101','yyyymmdd'))  - interval '1 sec'
--      left join ois_ods.sost change_sost on wm.well_id = change_sost.sk_1 and change_sost.dwh_is_active=true and 
--                                          change_sost.dwh_begin_date>=u.dwh_begin_date and change_sost.dwh_begin_date<=COALESCE(u.dwh_end_date,to_timestamp('20990101','yyyymmdd'))  - interval '1 sec'
--                                           and adw.dt>change_sost.dwh_begin_date 

--                                           
----  Пластовое распределение                        
--        left join ois_ods.skpl skpl on wm.well_id = skpl.sk_1 and skpl.dwh_is_active=true and r.pl_1=skpl.pl_1 and skv.ms_1 = skpl.ms_1 and (skpl.sk_1 > 110000000 and skpl.sk_1 < 119999999) and 
--                                     adw.dt>=skpl.dwh_begin_date and adw.dt<COALESCE(skpl.dwh_end_date,to_timestamp('20990101','yyyymmdd')) - interval '1 sec'	


                                                             
where 
WM.MEASURE_TYPE_ID in (30, 204, 1103, 1104, 33, 4, 3, 1, 11, 12, 7026, 7005)

--and sk_1=6400071300
           
group by SKV.S1_1,SKV.SK_1,  SKV.MS_1, SKV.lk_1, SKV.gu_1, SKV.om_1, SKV.pr_1, SKV.zx_1, SKV.st2_1, SKV.dn_1, SKV.db_1, SKV.pp_1, SKV.c1_1, date(adw.dt), SKV.KS_1, F.XR_1 --, SO.SS_1--,  S.GL_1          
            ) t