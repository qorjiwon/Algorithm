select PT_NAME, PT_NO, GEND_CD, AGE, case when TLNO is null then 'NONE' else TLNO end as TLNO
from PATIENT 
where age <= 12 and gend_cd='W'
order by age desc, pt_name