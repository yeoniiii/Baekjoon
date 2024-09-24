SELECT F.ID, N.FISH_NAME, F.LENGTH
FROM FISH_INFO AS F
    JOIN FISH_NAME_INFO AS N
    ON F.FISH_TYPE = N.FISH_TYPE
WHERE (F.FISH_TYPE, F.LENGTH) IN (SELECT FISH_TYPE, MAX(LENGTH)
                                 FROM FISH_INFO
                                 GROUP BY FISH_TYPE)
ORDER BY F.ID