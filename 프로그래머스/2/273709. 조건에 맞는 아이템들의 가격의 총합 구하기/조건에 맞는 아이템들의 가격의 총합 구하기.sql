select sum(price) as total_price
from (select * from item_info where rarity = 'legend') s