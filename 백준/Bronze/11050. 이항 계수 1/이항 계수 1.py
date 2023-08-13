N, K = map(int, input().split())

ans = 1
for k in range(K):
    ans *= N-k
    ans /= (k+1)
print(int(ans))