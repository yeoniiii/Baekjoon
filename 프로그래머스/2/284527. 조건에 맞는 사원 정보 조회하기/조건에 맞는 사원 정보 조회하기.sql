SELECT G.SCORE, G.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM (SELECT EMP_NO, SUM(SCORE) AS SCORE
      FROM HR_GRADE
      GROUP BY EMP_NO
      ORDER BY SUM(SCORE) DESC) AS G
      JOIN HR_EMPLOYEES AS E
      ON G.EMP_NO = E.EMP_NO
ORDER BY G.SCORE DESC
LIMIT 1