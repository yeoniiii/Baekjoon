N = int(input())
cost = [[]]
for i in range(N):
    cost.append(list(map(int, input().split())))

total_cost = [[0, 0, 0] for i in range(N+1)]

for i in range(1, N+1):
    total_cost[i][0] = cost[i][0] + min(total_cost[i-1][1], total_cost[i-1][2])
    total_cost[i][1] = cost[i][1] + min(total_cost[i-1][0], total_cost[i-1][2])
    total_cost[i][2] = cost[i][2] + min(total_cost[i-1][0], total_cost[i-1][1])
    
print(min(total_cost[N]))