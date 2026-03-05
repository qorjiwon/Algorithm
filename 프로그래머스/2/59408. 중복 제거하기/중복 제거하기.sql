SELECT count(*) as count
from (
    select * from animal_ins
    group by name
    having name is not null
) s