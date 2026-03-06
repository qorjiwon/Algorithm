SELECT HISTORY_ID, round(days*daily_fee,0) as fee
from (
    select c.car_id
    , history_id
    , datediff(END_DATE,START_DATE)+1 as days
    , case 
    when DISCOUNT_RATE is null then daily_fee 
    else daily_fee*(1-discount_rate*0.01) 
    end as daily_fee
    from CAR_RENTAL_COMPANY_CAR c 
          join CAR_RENTAL_COMPANY_RENTAL_HISTORY h
          on c.car_id = h.car_id
            left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p 
            on c.car_type = p.car_type and
                duration_type = case 
                when datediff(END_DATE,START_DATE)+1 >= 90 then '90일 이상'
                when datediff(END_DATE,START_DATE)+1 >= 30 then '30일 이상'
                when datediff(END_DATE,START_DATE)+1 >= 7 then '7일 이상'
                else null end
    where c.CAR_TYPE = '트럭'
     ) m
order by fee desc, HISTORY_ID desc