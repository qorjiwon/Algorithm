SELECT warehouse_id, warehouse_name, ADDRESS, 
case when freezer_yn is null then 'N' else freezer_yn end as freezer_yn
from FOOD_WAREHOUSE
where ADDRESS like '경기도%'
order by WAREHOUSE_ID