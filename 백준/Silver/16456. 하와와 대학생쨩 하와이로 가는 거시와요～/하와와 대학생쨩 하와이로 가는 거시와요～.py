N = int(input())
dp = [0] * (N+1)
dp[0], dp[1] = 1, 1
if N >= 2:
    dp[2] = 1
    for i in range(3, N+1):
        dp[i] = dp[i-1] % 1000000009 + dp[i-3] % 1000000009
print(dp[-1] % 1000000009)