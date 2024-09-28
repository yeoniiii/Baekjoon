SELECT D.YEAR, 
    M.MAX_SIZE - D.SIZE_OF_COLONY AS YEAR_DEV, 
    D.ID
FROM (SELECT *, YEAR(DIFFERENTIATION_DATE) AS YEAR
      FROM ECOLI_DATA) AS D
    LEFT OUTER JOIN (SELECT MAX(SIZE_OF_COLONY) AS MAX_SIZE,
                        YEAR(DIFFERENTIATION_DATE) AS YEAR
                     FROM ECOLI_DATA
                     GROUP BY YEAR) AS M
    ON D.YEAR = M.YEAR
ORDER BY D.YEAR, YEAR_DEV