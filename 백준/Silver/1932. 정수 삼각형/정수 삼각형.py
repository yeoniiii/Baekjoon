N = int(input())
num = [[]]
for i in range(N):
    num.append(list(map(int, input().split())))
    

route = [[0] * i for i in range(N+1)]

route[1] = num[1]
if N >= 2:
    route[2][0] = num[2][0] + route[1][0]
    route[2][1] = num[2][1] + route[1][0]
if N >= 3:
    for i in range(3, N+1):
        for j in range(i):
            if j == 0:
                route[i][j] = num[i][j] + route[i-1][j]
            elif j == i-1:
                route[i][j] = num[i][j] + route[i-1][j-1]
            else:
                route[i][j] = num[i][j] + max(route[i-1][j-1], route[i-1][j])

print(max(route[N]))