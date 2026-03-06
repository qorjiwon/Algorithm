SELECT APNT_NO, PT_NAME, a.PT_NO, d.MCDP_CD, DR_NAME, APNT_YMD
from APPOINTMENT a 
join PATIENT p on a.PT_NO = p.PT_NO
join doctor d on a.MDDR_ID = d.DR_ID
where year(APNT_YMD) = 2022 and month(APNT_YMD) = 4 and day(APNT_YMD)=13 and a.MCDP_CD = 'cs' and APNT_CNCL_YN = 'N'
order by APNT_YMD