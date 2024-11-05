import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
a, b, c = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cumsum = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        cumsum[i][j] = A[i-1][j-1] + cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1]

def get_sum(x1, y1, x2, y2):
    return cumsum[x2+1][y2+1] - cumsum[x1][y2+1] - cumsum[x2+1][y1] + cumsum[x1][y1]

ans = 10**9

for i in range(N-a+1):
    for j in range(M-b-c+1):
        ans = min(ans, get_sum(i, j, i+a-1, j+b+c-1))
       
for i in range(N-a-b+1):
    for j in range(M-c-a+1):
        ans = min(ans, get_sum(i, j, i+a-1, j+c-1)+get_sum(i+a, j+c, i+a+b-1, j+a+c-1))
        
for i in range(N-a-c+1):
    for j in range(M-b-a+1):
        ans = min(ans, get_sum(i, j, i+a-1, j+b-1) + get_sum(i+a, j+b, i+a+c-1, j+a+b-1))

print(ans)