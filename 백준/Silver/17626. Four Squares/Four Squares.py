n = int(input())
dp = [0] * (n+1)
dp[0] = 5

for i in range(1, n+1):
    if i ** (1/2) % 1 == 0:
        dp[i] = 1
    else:
        s = set()
        for j in range(int(i**(1/2)), 0, -1):
            if len(s) < 4:
                s.add(dp[j**2]+dp[i-j**2])
        dp[i] = min(s)

print(dp[-1])