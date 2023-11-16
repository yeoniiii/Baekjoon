-- 코드를 입력하세요
SELECT *
FROM PLACES P1
WHERE EXISTS (
    SELECT 1 FROM PLACES P2
    WHERE P1.HOST_ID = P2.HOST_ID
    GROUP BY HOST_ID
    HAVING COUNT(ID) >= 2)
ORDER BY ID ASC