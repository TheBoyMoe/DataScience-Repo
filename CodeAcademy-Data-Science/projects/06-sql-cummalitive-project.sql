delete from panels
where ID = 'ID';

delete from patients
where ID = 'ID';

select *
from patients limit
10;
select *
from panels limit
6;
select *
from recommended_values;

update patients
set status = 'active'
where ID = '7';

select *
from patients
where ID = '7';

create table inactive_patients as
select *
from patients
where status = 'inactive';

delete
from patients
where status = 'inactive';

select *
from inactive_patients;

alter table patients
rename to active_patients;

select *
from active_patients;

WITH
  total_active
  AS
  (
    SELECT COUNT(ID) AS 'active'
    FROM active_patients
  ),
  total_inactive
  AS
  (
    SELECT COUNT(ID) AS 'inactive'
    FROM inactive_patients
  ),
  total_patients
  AS
  (
    SELECT total_active.active + total_inactive.inactive AS 'total'
    FROM total_active, total_inactive
  )
SELECT
  (total_active.active*100 / total_patients.total) AS 'percent_active',
  (total_inactive.inactive*100 / total_patients.total) AS 'percent_inactive'
FROM total_active, total_inactive, total_patients;

select *
from active_patients
order by ID desc
limit 1;

--DELETE FROM active_patients 
--WHERE Name IN 
--(SELECT Name FROM active_patients LIMIT 1);

SELECT * 
FROM active_patients
WHERE ID =
(SELECT max(ID)
FROM active_patients);

select patient_ID, count(*) as 'count'
from panels
group by 1
having count(*) > 1
order by 2 desc;

alter table panels
add column LDL decimal
(5,2);

update panels
set LDL = panels.Cholesterol - (panels.HDL + panels.Triglycerides/5);

select *
from panels;

SELECT
  active_patients.Name AS 'Name',
  ROUND(LDL) AS 'LDL',
  active_patients.Address AS 'Address',
  active_patients.Phone AS 'Phone'
FROM
  panels,
  (SELECT Borderline_High, High
  FROM recommended_values
  WHERE Lipid = "LDL") rv
  JOIN active_patients ON panels.patient_ID = active_patients.ID
GROUP BY 
    LDL, 
    active_patients.Name
HAVING LDL >= rv.Borderline_High
ORDER BY LDL DESC;

SELECT
  COUNT(CASE WHEN (LDL >= rv.Borderline_High AND LDL < rv.High) THEN LDL END) AS Borderline_High,
  COUNT(CASE WHEN LDL >= rv.High THEN LDL END) AS High
FROM
  panels,
  (SELECT Borderline_High, High
  FROM recommended_values
  WHERE Lipid = "LDL") rv;