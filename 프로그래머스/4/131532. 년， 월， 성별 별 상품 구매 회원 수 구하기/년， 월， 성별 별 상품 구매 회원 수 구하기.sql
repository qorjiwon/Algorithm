select year(SALES_DATE) as YEAR, month(SALES_DATE) as MONTH, GENDER, count(DISTINCT a.user_id) as USERS
from ONLINE_SALE a left join USER_INFO b on a.USER_ID = b.USER_ID
where gender is not null
group by YEAR, MONTH, GENDER
order by year, month, gender