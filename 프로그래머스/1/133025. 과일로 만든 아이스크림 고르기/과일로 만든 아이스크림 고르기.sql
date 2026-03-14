select f.flavor
from FIRST_HALF f left join ICECREAM_INFO i on f.flavor = i.flavor
where total_order >= 3000 and INGREDIENT_TYPE = 'fruit_based'
order by total_order desc