select count(distinct gi.uwi) 
--gi.hef, gi.h, gi.date_op, gi.contractor_qj 
from geobd_ods.grp_info gi
where (uwi like '036_%')
-- or uwi like '313_%'
and gi.hef is not null and gi.contractor_qj is not null
limit 20


select dgk.code, dgk.sdes 
from geobd_ods.dict_g_kshd dgk
where dgk.sdes is not null
and dgk.description like 'ЕТЫ%'
or dgk.description like 'ВЫНГ%'
order by 1

select f.wellbore, f.layer, f.gross_pay, f.frac_date 
from rdfsmart_ods.frac f 
where f.oil_field like 'Еты%'
and f.layer is not null


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
--c.table_schema='wellop_ods' --название схемы
--and c.table_name='well_op_oil_daily' -- название таблицы
--and c.column_name like '%vdp%' -- это конкретное поле
--and 
pgd.description like '%ероприят%' and c.table_schema not like 'dm_%'
--group by c.table_schema 
order by 1

select description, schema_name  
from pg_catalog.pg_description pgd 
join 
	(SELECT to_regnamespace(schema_name)::oid as id,schema_name  
	 FROM information_schema.schemata s) a 
on pgd.objoid =a.id
order by 2


select mos.well_id, mos.oil_production, oil_rate, property_date 
from cds_ods.move_out_sheet mos 
where mos.well_id in (	select sk_1
						from ois_ods.fond f
						where ms_1 = 'MS0611'
						and s1_1 in ('1758', '2067'))
order by 4 desc 


select z.dz_1, z.sk_1, z.qj_1 
from ois_ods.zam z 
where ms_1 = 'MS0611' and sk_1 in (	select sk_1
						from ois_ods.fond f
						where ms_1 = 'MS0611'
						and s1_1 in ('1758'))
order by 1 desc

