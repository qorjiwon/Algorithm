select SCORE, e.EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_EMPLOYEES e 
    left join HR_DEPARTMENT d on e.DEPT_ID = d.DEPT_ID
    left join ( select EMP_NO, sum(SCORE) as score
                from HR_GRADE
                group by EMP_NO
                ) g 
        on e.EMP_NO = g.EMP_NO
order by score desc
limit 1


