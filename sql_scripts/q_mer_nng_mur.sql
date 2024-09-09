--�������� �������� ������������� �� ��
select distinct org_name, vwn.field_name, vwn.field_id 
from wellop_ods.v_wf_nt vwn 
where vwn.org_name like '%���%' or vwn.org_name like '%�����%'
order by 2

--�������� ��� �� ���� ��������� ���� ������������� ��
select * 
from rdfsmart_ods.mer_v mv 
where oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%���%' or vwn.org_name like '%�����%')	
limit 10

--�������� ����� �� ���� ��������� ���� ������������� ��
select count(distinct wellbore) as "not dwh"
from rdfsmart_ods.rigis rg 
where oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%���%' or vwn.org_name like '%�����%')
--and dwh_is_active is true 
and oil_field = '����������'
--limit 50					


--�������� ��������� ������ �� ���� ��������� ���� ������������� ��
select oil_field, objectname as pad_num,x_center, y_center, well
--select count(well)
from rdfsmart_ods.wellcluster w 
where x_center > 0 and oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%���%' or vwn.org_name like '%�����%')

					
--�������� ������� �������� ������� ��� � ����� �� ����� ���
select field_gbd, uwi as well_geobd, skv_ngt as well_ngt  
from geobd_ods.wellinfo w 
order by 1


--�������� ���������� �� ���� ��������� ���� ������������� ��
select *
from rdfsmart_ods.perf p 
where oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%���%' or vwn.org_name like '%�����%')
order by 1


--�������� ���������� ������� � ����������� ������ �� SQL
select concat(lower(oil_field),'_',wellbore) as uwi, oil_field,wellbore,x,y,z,zabs
from rdfsmart_ods.trajectory t
where oil_field in (
					select distinct field_name 
					from wellop_ods.v_wf_nt vwn 
					where vwn.org_name like '%���%' or vwn.org_name like '%�����%')
			
					
--��� ��� � ������ �� �� ���������� � �� ��� � ������� ����
select f.oil_field, f.wellbore, f.contractor, f.frac_date, f.perf_top, 
f.perf_bottom, f.proppant_total 
from rdfsmart_ods.frac f
where f.oil_field like '%�����%' and (f.wellbore like '1950%' or f.wellbore like '1758%'
or f.wellbore like '2067%')


select oil_field , wellbore, layer, contractor, frac_date, remarks, proppant_total 
from rdfsmart_ods.frac f 
where dwh_is_active is true and oil_field like '����������' and wellbore = '1'

--�������� �������� ������ � ��������� �����
select
    c.table_schema,
    c.table_name,
    c.column_name,
    pgd.description
from pg_catalog.pg_statio_all_tables as st -- ���������� �� ��������
inner join pg_catalog.pg_description pgd -- ����������� � �������� 
       on  pgd.objoid = st.relid
inner join information_schema.columns c on -- ��������� ������
    pgd.objsubid   = c.ordinal_position and
    c.table_schema = st.schemaname and
    c.table_name   = st.relname
where 
c.table_schema='rdfsmart_ods' --�������� �����
and c.table_name='frac' -- �������� �������
--and c.column_name like '%vdp%' -- ��� ���������� ����
--and 
--and pgd.description like '%���%'
order by 1