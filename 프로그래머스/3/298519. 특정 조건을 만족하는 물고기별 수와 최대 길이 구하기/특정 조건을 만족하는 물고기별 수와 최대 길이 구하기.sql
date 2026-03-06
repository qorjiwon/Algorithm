select FISH_COUNT, max_LENGTH, FISH_TYPE
from (
    select count(*) as FISH_COUNT
    , FISH_TYPE
    , avg(case when LENGTH is null then 10 else length end) as avg_length
    , max(length) as max_length
    from FISH_INFO
    group by fish_type
) m 
where avg_length >= 33
order by FISH_TYPE