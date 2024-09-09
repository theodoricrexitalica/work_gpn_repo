--Выгрузка ригис по ГС Карамовки из ГеоБД
with drill_dt as (select wi.uwi, wi.insert_date, wi.cnt_bore, wi.type_bore 
				from geobd_ods.wellinfo wi 
				where wi.do_gbd = 'ГПН-ННГ' 
				and insert_date between '2022-01-01' and '2023-01-01'
				and lower(wi.field_gbd) like '%арамов%'
				and wi.type_bore like '%горизонтальная%')
select lower(w.field_gbd) as oilfield, r.uwi, r.well_name ,layers_name_r, r.colprop,
top_md,h,dg.description as litho, dg2.description as satur_descr, rp,
dt.insert_date::date, dt.cnt_bore, dt.type_bore
from geobd_ods.rigis r 
join geobd_ods.wellinfo w on r.uwi = w.uwi
join drill_dt dt on w.uwi = dt.uwi
join geobd_ods.dict_g dg on r.lithology_id = dg.id
join geobd_ods.dict_g dg2 on r.saturation_prin_id = dg2.id 
where r.uwi in (select w.uwi
				from geobd_ods.wellinfo w 
				where w.do_gbd = 'ГПН-ННГ' 
				and insert_date between '2022-01-01' and '2023-01-01'
				and lower(w.field_gbd) like '%арамов%'
				)
order by dt.insert_date desc
							
--Выгрузка скважин за 2022 год от ННГ
select do_gbd, field_gbd, uwi, well_state, skv_ngt, insert_date, type_bore,count(uwi) over (partition by do_gbd) 
from geobd_ods.wellinfo w 
where w.do_gbd = 'ГПН-ННГ' and insert_date between '2022-01-01' and '2023-01-01'
--where w.do_gbd = 'ГПН-Хантос' and insert_date between '2022-01-01' and '2023-01-01'
--and uwi like '%PL'
order by 1,5, 4 desc

select distinct type_bore, well_count_tb, well_sum
from (
		select field_gbd, w.type_bore, 
		count(uwi) over (partition by type_bore) as well_count_tb, 
		count(uwi) over (partition by field_gbd) as well_sum  
		from geobd_ods.wellinfo w 
		where w.do_gbd = 'ГПН-Хантос' and insert_date between '2022-01-01' and '2023-01-01'
		and w.field_gbd = 'ПРИОБСКОЕ'
		order by 3 desc) as sq1
order by 2 desc



