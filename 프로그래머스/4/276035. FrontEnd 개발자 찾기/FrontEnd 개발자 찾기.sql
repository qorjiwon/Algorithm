select id, email, first_name, last_name
from SKILLCODES s join DEVELOPERS d on s.code&d.skill_code > 0
where category = "front end"
group by id, email, first_name, last_name
order by id