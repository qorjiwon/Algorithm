SELECT ANIMAL_ID, name
from ANIMAL_INS
where animal_type = 'dog' and name like '%el%'
order by name