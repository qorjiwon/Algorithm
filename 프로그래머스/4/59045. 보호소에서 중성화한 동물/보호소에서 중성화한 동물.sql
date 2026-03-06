SELECT i.animal_id, i.animal_type, i.name
from animal_ins i join animal_outs o on i.animal_id = o.animal_id
where (sex_upon_intake not like 'Neutered %' and sex_upon_outcome like 'Neutered %')
or
(sex_upon_intake not like 'Spayed %' and sex_upon_outcome like 'Spayed %')
order by i.animal_id