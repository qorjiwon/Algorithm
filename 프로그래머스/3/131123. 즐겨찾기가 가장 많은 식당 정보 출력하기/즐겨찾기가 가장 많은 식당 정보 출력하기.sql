select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from (select *, rank() over (partition by food_type order by favorites desc) as rnk from REST_INFO) as m
group by FOOD_TYPE
order by FOOD_TYPE desc