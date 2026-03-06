SELECT distinct c.CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h 
    join CAR_RENTAL_COMPANY_CAR c
    on h.CAR_ID = c.CAR_ID
where c.CAR_TYPE = '세단' and month(start_date) = 10
order by c.car_id desc