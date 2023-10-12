N = int(input())
stair = []
for n in range(N):
    stair.append(int(input()))

dp = [0] * N
dp[0] = stair[0]

if N == 1: 
    print(dp[0])
elif N==2:
    print(stair[0] + stair[1])
else:
    dp[1] = stair[0] + stair[1]
    dp[2] = max(stair[0], stair[1]) + stair[2]
    for i in range(3, N):
        dp[i] = max(dp[i-3] + stair[i-1], dp[i-2]) + stair[i]
    print(dp[-1])