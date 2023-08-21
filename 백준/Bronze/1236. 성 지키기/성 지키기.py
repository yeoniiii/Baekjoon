N, M = map(int, input().split())
s = 0
row = [0]*M

for _ in range(N):
    arr = list(input())
    if not 'X' in arr:
        s += 1
    else: 
        for m in range(M):
            if arr[m] == 'X':
                row[m] = 1
print(max(M-sum(row), s))