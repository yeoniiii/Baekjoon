N = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))
cost, i, id = 0, 0, 1

while i + id < N:
    if oil[i] > oil[i + id]:
        cost += oil[i] * sum(dist[i:(i+id)])
        i += id
        id = 1
    else:
        id += 1
else:
    cost += oil[i] * sum(dist[i:])

print(cost)