with M as (
select * from FIRST_HALF
union all
select * from july
)

select flavor from M
group by flavor
order by sum(total_order) desc
limit 3