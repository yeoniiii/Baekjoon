N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input()))

def color(a, b):
    cnt = 0
    for m in range(M):
        for i in range(N):
            if i < a:
                if arr[i][m] != 'W':
                    cnt += 1
            elif i < b:
                if arr[i][m] != 'B':
                    cnt += 1
            else:
                if arr[i][m] != 'R':
                    cnt += 1
    return cnt

from itertools import combinations

min_cnt = N*M
for (a, b) in combinations(range(1, N), 2):
    cnt_i = color(a, b)
    if min_cnt > cnt_i:
        min_cnt = cnt_i
print(min_cnt)