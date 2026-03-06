select a.FOOD_TYPE, REST_ID, REST_NAME, a.FAVORITES
from REST_INFO a
join (SELECT FOOD_TYPE, max(FAVORITES) as FAVORITES from REST_INFO group by FOOD_TYPE) b
    on a.food_type = b.food_type and a.favorites = b.favorites
group by a.FOOD_TYPE
order by a.FOOD_TYPE desc