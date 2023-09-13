N = int(input())
height = []
weight = []
rank = [1] * N

for _ in range(N):
    x, y = map(int, input().split())
    height.append(x)
    weight.append(y)

for i in range(N):
    for j in range(N):
        if height[i] < height[j] and weight[i] < weight[j]:
            rank[i] += 1

print(*rank)
    