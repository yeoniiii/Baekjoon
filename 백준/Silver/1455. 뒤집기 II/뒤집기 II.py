import sys
input = lambda: sys.stdin.readline().rstrip()

arr = []
N, M = map(int, input().split())
for i in range(N):
    arr.append(list(input()))
cnt = 0

for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if arr[i][j] == '1':
            cnt += 1
            for p in range(i+1):
                for q in range(j+1):
                    if arr[p][q] == '1':
                        arr[p][q] = '0'
                    else:
                        arr[p][q] = '1'
print(cnt)