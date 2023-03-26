N, K = map(int, input().split())
cnt = 0
for i in range(1, N+1):
    if cnt == K: break
    elif N%i == 0:
        cnt += 1
        factor = i
if cnt < K: factor=0
print(factor)