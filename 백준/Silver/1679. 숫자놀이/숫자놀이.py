N = int(input())
num = list(map(int, input().split()))
K = int(input())
dp = [i for i in range(1001)]
stop = 0

for n in num:
    dp[n] = 1
for i in range(2, 1001):
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i-j] + dp[j])
    if dp[i] > K:
        stop = i
        break
if stop % 2 == 0:
    winner = 'holsoon'
else:
    winner = 'jjaksoon'
print(f"{winner} win at {stop}")