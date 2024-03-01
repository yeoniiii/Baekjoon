N = int(input())
cost = [[]]
for i in range(N):
    cost.append(list(map(int, input().split())))

def rgb(start):
    total_cost = [[10**6] * 3 for _ in range(N+1)]
    total_cost[1][start] = cost[1][start]

    for h in range(2, N+1):
        for j in range(3):
            for k in range(3):
                if j!=k and total_cost[h][j] > cost[h][j] + total_cost[h-1][k]:
                    if h < N or (h==N and j!= start):
                        total_cost[h][j] = cost[h][j] + total_cost[h-1][k]
                    
    return min(total_cost[N])

print(min(rgb(0), rgb(1), rgb(2)))