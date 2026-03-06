SELECT b.AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(price*sales) as TOTAL_SALES
from BOOK b 
join author a 
    on a.author_id = b.author_id
join book_sales s 
    on b.book_id = s.book_id
where year(s.SALES_DATE) = 2022 and month(s.SALES_DATE) = 1
group by AUTHOR_NAME, CATEGORY
order by b.AUTHOR_ID, CATEGORY desc