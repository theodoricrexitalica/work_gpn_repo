select distinct vwn.field_name, sb.s1_1, sb.zb2_1, 
to_date(sb.dn_1::varchar,'YYYYMMDD'), 
to_date(sb.db_1::varchar,'YYYYMMDD'),
to_date(sb.db_1::varchar,'YYYYMMDD') - to_date(sb.dn_1::varchar,'YYYYMMDD') as diff,
sb.c1_1, c.ne_1,
sb.dwh_is_active, sb.np_1 
from ois_ods.spskv_bore sb 
join wellop_ods.v_wf_nt vwn on sb.ms_1 = vwn.field_id
join ois_ods.class c on sb.c1_1 = c.cd_1 
--join ois_ods.class c2 on sb.ne_1 = c.cd_1 
where lower(vwn.field_name) like '%угмут%' and sb.s1_1 in ('1758', '1950','2067')

select c.cd_1, c.ne_1 
from ois_ods.class c
where cd_1 like 'NP%'
order by 1

--Поиск месторождений по ДО
select distinct field_name 
from wellop_ods.v_wf_nt vwn 
where vwn.org_name like '%ННГ%'
order by 1

--Поиск скважин, кустов, месторождений
select well_id, well_name, well_cluster, field_id, field_name
from wellop_ods.v_well_full
where field_name like 'Восточно-Пякутинское' and well_cluster = '4'
--where field_name like '%ессоях%'

--Поиск минимальной и максимальной дат для выгрузки замеров
select min(mindate), max(maxdate)
from (
		select z.sk_1, min(z.dwh_end_date) as mindate, max(z.dwh_end_date) as maxdate
		from ois_ods.zam z
		where z.sk_1 in (select well_id
						from wellop_ods.v_well_full
						where field_name like 'Восточно-Пякутинское' and well_cluster = '4')
		group by z.sk_1) as sq

--Пластовые давления ВДП
select field_name as "field", well_number "well", layer_shut_pressure "p_plast", vdp_pressure "p_plast_vdp", 
layer_shut_pressure_date "date", manual_layer_shut_pressure "manual_corr_pplast"
from wellop_ods.v_well_op_metering vwom 
where field_id like 'MS0011' 


--Поиск названий замеров по их id
select id, long_name, estimation_method, cds_table, exactness,
dwh_is_active, fact_op_field
from wellop_ods.measure_type mt 
where (long_name like 'Обводненность %' 
or long_name like 'Дебит нефт%'
or long_name like 'Дебит жидк%'
or long_name like 'Давление пласт%')
--and cds_table is not null 
--and id in (1, 3, 4, 11, 12, 30, 33, 101, 122, 128, 204, 1103, 1104,  7005, 7132, 7247)
order by 2 desc
--where id in (1, 3, 4, 11, 12, 30, 33, 101, 122, 128, 204, 1103, 1104,  7005, 7132, 7247)

--Поиск названий замеров по их id
select id, long_name, estimation_method, cds_table, exactness,
dwh_is_active, fact_op_field
from wellop_ods.measure_type mt 
where id in (30, 204, 1103, 1104, 33, 4, 3, 1, 11, 12, 7026, 7005)


--Выгрузка описаний таблиц в указанной схеме
select
    c.table_schema,
    c.table_name,
    c.column_name,
    pgd.description
from pg_catalog.pg_statio_all_tables as st -- статистика по таблицам
inner join pg_catalog.pg_description pgd -- комментарии к столбцам 
       on  pgd.objoid = st.relid
inner join information_schema.columns c on -- структура таблиц
    pgd.objsubid   = c.ordinal_position and
    c.table_schema = st.schemaname and
    c.table_name   = st.relname
where 
c.table_schema='smb_ods' --название схемы
--c.table_schema='wellop_ods' --название схемы)
--and pgd.description like '%пласт%'
--or pgd.description like '%ластовое%'
--and pgd.description like '%Pпл%' 
and pgd.description like '%ЗБС%'
--and c.table_name='layer_mapping' -- название таблицы
--and c.column_name like '%vdp%' -- это конкретное поле
--and pgd.description
order by 1

select pgd.description, a.schema_name 
from pg_catalog.pg_description pgd 
join (SELECT to_regnamespace(schema_name)::oid as id,schema_name  
FROM information_schema.schemata s  ) a on pgd.objoid =a.id
order by 1

select * from pg_catalog.pg_description pgd where objoid = (SELECT to_regnamespace('rdfsmart_ods')::oid)

select well_id, layer_name, vdp_pressure, vdp_pressure_date, calc_date 
from wellop_ods.v_well_op vwo
limit 30

select *
from wellop_ods.v_well_full vwf 


--Тестирование выгрузку геол названий пластов, скважин, месторождений
select distinct(pl.sk_1), ww.well_name, pl_1, vmwo.layer_name, pl.ms_1, ww.field_name, pl.st2_1 
from ois_ods.plast pl
join wellop_ods.v_well_full ww on 
		ww.field_id = pl.ms_1
join wellop_ods.v_misc_well_op vmwo on
		vmwo.layer_id = pl.pl_1
join wellop_ods.v_well_full on
		ww.well_id = pl.sk_1 
where ww.field_name in ('Восточно-Мессояхское')
		

--Выгрузка комментариев ко всем схемам		
select description, schema_name  
from pg_catalog.pg_description pgd 
join 
	(SELECT to_regnamespace(schema_name)::oid as id,schema_name  
	 FROM information_schema.schemata s) a 
on pgd.objoid =a.id
order by 2

--Поиск геологических и ID номеров скважин по месторождениям и кустам
select well_id, well_name, well_cluster, field_name
from wellop_ods.v_well_full
where field_name in ('Восточно-Мессояхское')
and trim(well_name) in ('15', '1299', '477', '446', '1503', '1600', '470', '508', '5290',
       '476', '307', '1307', '352', '504', '353', '662', '382', '631',
       '1439', '447', '165', '1471', '3062', '301', '1134', '420', '500',
       '3045', '682', '1438', '325', '298', '592', '3035', '1382', '3048',
       '1279', '1691', '746', '1595', '3056', '1596', '13', '438', '305',
       '1507', '600', '538', '501', '633', '621', '766', '289', '618',
       '1102', '540', '1509', '629', '1157', '157', '709', '4011', '1661',
       '186', '3021', '1410', '619', '386', '46ПО', '431', '1690', '588',
       '205', '14', '181', '444', '472', '34', '162', '1132', '1381',
       '247', '249', '166', '1480', '507', '360', '510', '541', '12',
       '5026', '250', '655', '8031', '8070', '1739', '6807', '206',
       '8052', '6214', '2в', '243', '620', '321', '776', '6317', '237',
       '4278', '4227', '194', '74', '138', '192', '6830', '4225', '3057',
       '4010', '356', '4110', '384')
       
--Скрипт от Рахматуллина по поиску айдишника
select g.uidwellbore, g.localityname, g.wellname, g.welltype, 
g.linercompany, g.drillendplan, g.targetoffset, g.hlength 
from smb_ods.gtm g, dm_vosr.v_wellbores w
where w.nsi_well_id = g.nsiwell 
limit 10


select lower(w.field_gbd), r.well_name ,layers_name_r,top_md,h,top_tvd,hif,
lit,sat,sat_pr,
rp,kgl,kp,kpr,kng,kvo
from geobd_ods.rigis r 
join geobd_ods.wellinfo w on r.uwi = w.uwi
where lower(w.field_gbd) in (
							select distinct lower(field_name)
							from wellop_ods.v_wf_nt vwn 
							where vwn.org_name like '%ННГ%' or vwn.org_name like '%Мурав%')


select max(mv.date_)
from rdfsmart_raw.mer_v mv
where lower(mv.oil_field) in (
							select distinct lower(field_name)
							from wellop_ods.v_wf_nt vwn 
							where vwn.org_name like '%ННГ%' or vwn.org_name like '%Мурав%')
--order by dwh_updated desc, date_ desc  
--limit 10
							

							
--Т.к. МЭРы из NGT больше не работают, там данные только по 12.2022 делаю тут огромный запрос
--по выгрузке МЭРов из OIS
select a.ms_1, a.s1_1, gg_1, a.dd_1, xr_1,c2.ne_1,a.sp_1, c.ne_1, a.pl_1, vwo.layer_name 
from ois_ods.arx a
--join ois_ods.class c on a.sp_1 = c.cd_1
--join ois_ods.class c2 on a.xr_1 = c2.cd_1
--join wellop_ods.v_well_op vwo on a.pl_1 = vwo.layer_id 
--join wellop_ods.v_well_full vwf on a.sk_1 = vwf.well_id 
where dwh_is_active is true 
order by 1 desc,2 desc
limit 20

--поиск названий пластов
select vwo.layer_id, vwo.layer_name
from wellop_ods.v_well_op vwo 

--поиск названий ДО и месторождений
select vwf.field_id , vwf.field_name, vwf.well_id, vwf.org_name 
from wellop_ods.v_well_full vwf 
where vwf.org_name = 'АО "Газпромнефть - ННГ"'


--Поиск типа скважина на месторождении с датой добуривания
select wp.wellname , wp.welltype, wp.localityname , wp.drillendfact 
from smb_ods.well_phase wp  
where wp.localityname like '%угмут%' 
and wp.welltype like '%+П%'
order by 4 desc 

select 
w.nsi_asset_operator_name, w.nsi_field_name, 
w.nsi_well_name as wnum, w.nsi_wellbore_name as wbname, w.nsi_wellbore_number as wbnum, 
--oaw.ois_layer_id,l.ois_layer_name, l.ngt_development_object, l.ngt_layer_name,
dn_1, xr_1, begin_date 
from dm_vosr.ois_arx_wellbore oaw 
join dm_vosr.wellbores w on oaw.nsi_wellbore_id = w.nsi_wellbore_id 
join dm_vosr.layers l on oaw.ois_layer_id = l.ois_layer_id 
where w.nsi_asset_operator_name like '%ННГ%'
order by begin_date desc 
limit 15


select *
from dm_vosr.ois_wellbores ow 
--where id='XR0020'

select max(mv.date_) 
from rdfsmart_ods.mer_v mv 
