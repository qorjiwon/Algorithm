SELECT month(START_DATE) as MONTH, CAR_ID, count(*) as RECORDS
from (select *
      from CAR_RENTAL_COMPANY_RENTAL_HISTORY
      where start_date between '2022-08-01' and '2022-10-31'
        and
        car_id in (
            select car_id
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
            where start_date between '2022-08-01' and '2022-10-31'
            group by car_id
            having count(*) >= 5        
        )
     ) m
group by MONTH, CAR_ID
order by MONTH, CAR_ID desc