T = int(input())
cases = []
for t in range(T):
    cases.append(int(input()))
    
dp = [[0, 0] for _ in range(max(cases)+1)]
dp[1] = [1, 0]
dp[2] = [1, 1]
dp[3] = [2, 2]

for i in range(4, max(cases)+1):
    dp[i][0] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1]) % 1000000009
    dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % 1000000009

for case in cases:
    print(*dp[case])