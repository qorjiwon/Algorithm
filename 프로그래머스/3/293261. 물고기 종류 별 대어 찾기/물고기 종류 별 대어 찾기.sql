select a.id, b.fish_name, a.length
from fish_info a 
join fish_name_info b on a.fish_type = b.fish_type
join (
    select fish_type, max(length) as length from fish_info group by fish_type
) c on a.fish_type = c.fish_type and a.length = c.length
order by a.id