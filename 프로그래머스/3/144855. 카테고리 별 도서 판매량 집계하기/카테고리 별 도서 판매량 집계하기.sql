SELECT b.CATEGORY, sum(sales) as TOTAL_SALES
from BOOK_SALES a left join book b on a.book_id = b.book_id
where month(SALES_DATE) = 1
group by b.CATEGORY
order by b.CATEGORY