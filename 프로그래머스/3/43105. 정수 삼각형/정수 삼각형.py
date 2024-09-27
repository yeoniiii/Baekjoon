def solution(triangle):
    dp = [[0] * (i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for row in range(1, len(triangle)):
        dp[row][0] = dp[row-1][0] + triangle[row][0]
        dp[row][row] = dp[row-1][row-1] + triangle[row][row]
        for i in range(1, row):
            dp[row][i] = max(dp[row-1][i-1], dp[row-1][i]) + triangle[row][i]
    return max(dp[-1])