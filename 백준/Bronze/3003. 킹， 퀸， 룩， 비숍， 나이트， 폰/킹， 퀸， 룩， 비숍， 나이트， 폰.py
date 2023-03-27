find = list(map(int, input().split()))
set = [1, 1, 2, 2, 2, 8]
need = []

for i in range(6):
    need.append(set[i] - find[i])
print(' '.join(map(str, need)))
