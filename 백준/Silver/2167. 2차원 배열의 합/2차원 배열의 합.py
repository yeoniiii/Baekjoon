N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(1, M):
        arr[i][j] += arr[i][j-1]

K = int(input())
for k in range(K):
    s = 0
    i, j, x, y = map(int, input().split())
    for row in range(i-1, x):
        if j == 1:
            s += arr[row][y-1]
        else:
            s += arr[row][y-1] - arr[row][j-2]
    print(s)