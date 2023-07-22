paper = [[0]*101 for _ in range(101)]
N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    for x in range(a, a+10):
        for y in range(b, b+10):
            paper[x][y] = 1

area = 0
for r in range(101):
    area += paper[r].count(1)
print(area)