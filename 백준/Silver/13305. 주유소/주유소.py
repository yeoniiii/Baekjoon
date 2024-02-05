N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
cost = 0
for i in range(len(road)):
    if road[i] == 0:
        pass
    elif oil[i] >= oil[i+1]:
        cost += oil[i] * road[i]
        road[i] = 0
    else:
        cost += oil[i] * (road[i] + road[i+1])
        road[i] = road[i+1] = 0
print(cost)
        