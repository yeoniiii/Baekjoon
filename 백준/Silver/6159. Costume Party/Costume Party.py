import sys
input = lambda: sys.stdin.readline().rstrip()

N, S = map(int, input().split())
L = []
for i in range(N):
    L.append(int(input()))
L.sort()
cnt = 0
i, j = 0, N-1
while i < j:
    s = L[i] + L[j]
    if s > S:
        j -= 1
    else:
        cnt += j - i
        i += 1
print(cnt)           