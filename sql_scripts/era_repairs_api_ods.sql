select *
from era_repairs_api_ods.well_event we 
--join era_repairs_api_ods.event_type et on we.welleventid = et.id
--inner join era_repairs_api_ods.brigade b on we.affiliateid = b.affiliateid 
where field like '%ессоях%'
and trim(well) in ('15', '1299', '477', '446', '1503', '1600', '470', '508', '5290',
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

       
       
select *
from era_repairs_api_ods.event_type et 

select eventname, field, well,"cluster", gtmdata_begindatefact, gtmdata_description, dwh_is_active,
gtmdata_layeraftername, gtmdata_contractorgrporkrs
--field, well, gtmdata_contractorgrporkrs, gtmdata_layer, gtmdata_propant, 
--gtmdata_begindatefact 
from era_repairs_api_ods.well_event we 
where ((field like '%угму%' and well like '2645%') or 
(field like '%ынгап%' and well like '5242%')) and dwh_is_active is true
group by eventname, field, well, "cluster", gtmdata_begindatefact, gtmdata_description, dwh_is_active,
gtmdata_layeraftername, gtmdata_contractorgrporkrs
--limit 5

--select g.localityname, g.wellname, 
select g.uidwell, g.localityname, g.wellname, g.welltype, 
g.linercompany, g.drillendplan, g.targetoffset, g.hlength 
from smb_ods.gtm g
join nsi_ods.brd_wells bw on g.uidwell = bw.guid
where g.linercompany = 'ООО "НОВ Комплишн Тулз"' 
or (wellname = '5242' and g.localityname = 'Вынгапуровское')
--order by 5

select *
from nsi_ods.
	
select w.uwi, w.field_gbd 
from geobd_ods.wellinfo w
where lower(w.field_gbd) in (select lower(g.localityname)
						 from smb_ods.gtm g 
						 where g.linercompany = 'ООО "НОВ Комплишн Тулз"' or 
						 (wellname = '5242' and g.localityname = 'Вынгапуровское'))
and SUBSTRING(w.well_name, '[0-9]+') in (select g.wellname
											from smb_ods.gtm g 
											where g.linercompany = 'ООО "НОВ Комплишн Тулз"' or 
											(wellname = '5242' and g.localityname = 'Вынгапуровское'))		

											
select gf.gbd_wellbore_id, gf.start_date, gf.start_liq_rate, gf.start_oil_rate 
from dm_vosr.geobd_frac gf 
--where gf.gbd_wellbore_id in (select w.uwi
--							from geobd_ods.wellinfo w
--							where lower(w.field_gbd) in (select lower(g.localityname)
--													 from smb_ods.gtm g 
--													 where g.linercompany = 'ООО "НОВ Комплишн Тулз"' or 
--													 (wellname = '5242' and g.localityname = 'Вынгапуровское'))
--							and SUBSTRING(w.well_name, '[0-9]+') in (select g.wellname
--													from smb_ods.gtm g 
--													where g.linercompany = 'ООО "НОВ Комплишн Тулз"' or 
--													(wellname = '5242' and g.localityname = 'Вынгапуровское')))
where gf.start_liq_rate is not null


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
c.table_schema='nsi_ods' --название схемы
--and c.table_schema='well_event' --название схемы)
--and c.table_name='well_event' -- название таблицы
--and c.column_name like '%vdp%' -- это конкретное поле
--and pgd.description
order by 2