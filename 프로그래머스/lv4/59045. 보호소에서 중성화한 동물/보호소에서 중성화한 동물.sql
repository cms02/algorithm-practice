-- 코드를 입력하세요
SELECT A.*
FROM
(SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I
WHERE SEX_UPON_INTAKE LIKE '%Intact%') A
JOIN ANIMAL_OUTS O USING(ANIMAL_ID)
WHERE O.SEX_UPON_OUTCOME NOT LIKE '%Intact%'
