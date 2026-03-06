select count(*) as FISH_COUNT, month(time) as month
from FISH_INFO
group by month
order by month