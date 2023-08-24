M = int(input())
cup = [1, 0, 0]

for m in range(M):
    x, y = map(int, input().split())
    save = cup[x-1]
    cup[x-1] = cup[y-1]
    cup[y-1] = save
print(cup.index(1)+1)