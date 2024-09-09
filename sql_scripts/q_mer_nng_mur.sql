--Выгрузка названий месторождений по ДО
select distinct org_name, vwn.field_name, vwn.field_id 
from wellop_ods.v_wf_nt vwn 
where vwn.org_name like '%ННГ%' or vwn.org_name like '%Мурав%'
order by 2

--Выгрузка МЭР по всем скважинам всех месторождений ДО
select * 
from rdfsmart_ods.mer_v mv 
where oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%ННГ%' or vwn.org_name like '%Мурав%')	
limit 10

--Выгрузка РИГИС по всем скважинам всех месторождений ДО
select count(distinct wellbore) as "not dwh"
from rdfsmart_ods.rigis rg 
where oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%ННГ%' or vwn.org_name like '%Мурав%')
--and dwh_is_active is true 
and oil_field = 'Сугмутское'
--limit 50					


--Выгрузка координат кустов по всем скважинам всех месторождений ДО
select oil_field, objectname as pad_num,x_center, y_center, well
--select count(well)
from rdfsmart_ods.wellcluster w 
where x_center > 0 and oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%ННГ%' or vwn.org_name like '%Мурав%')

					
--Выгрузка словаря названий скважин НГТ и ГеоБД по всему ГПН
select field_gbd, uwi as well_geobd, skv_ngt as well_ngt  
from geobd_ods.wellinfo w 
order by 1


--Выгрузка перфораций по всем скважинам всех месторождений ДО
select *
from rdfsmart_ods.perf p 
where oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%ННГ%' or vwn.org_name like '%Мурав%')
order by 1


--Выгрузка траекторий скважин с подготовкой данных на SQL
select concat(lower(oil_field),'_',wellbore) as uwi, oil_field,wellbore,x,y,z,zabs
from rdfsmart_ods.trajectory t
where oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%ННГ%' or vwn.org_name like '%Мурав%')
			
					
--Ищу ЗБС и данные по их перфорации в БД НГТ в таблице фрак
select f.oil_field, f.wellbore, f.contractor, f.frac_date, f.perf_top, 
f.perf_bottom, f.proppant_total 
from rdfsmart_ods.frac f
where f.oil_field like '%угмут%' and (f.wellbore like '1950%' or f.wellbore like '1758%'
or f.wellbore like '2067%')


select oil_field , wellbore, layer, contractor, frac_date, remarks, proppant_total 
from rdfsmart_ods.frac f 
where dwh_is_active is true and oil_field like 'Сугмутское' and wellbore = '1'

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
c.table_schema='rdfsmart_ods' --название схемы
and c.table_name='frac' -- название таблицы
--and c.column_name like '%vdp%' -- это конкретное поле
--and 
--and pgd.description like '%ГРП%'
order by 1