import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, D = map(int, input().split())
h = []
for i in range(N):
    h_i = sorted(list(map(int, input().split())))
    h_i = [h+D*(i+1) for h in h_i]
    h.append(h_i)
    
t = 0
for j in range(M):
    for i in range(1, N):
        if h[i-1][j] >= h[i][j]:
            t += 1
if t == 0:
    print("YES")
else:
    print("NO")