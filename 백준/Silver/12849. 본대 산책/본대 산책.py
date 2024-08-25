D = int(input())
graph = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [2, 3, 5, 7], [3, 4, 6], [5, 7], [6, 4]]
prev = {}
prev[0] = 1
for i in range(D):
    curr = {}
    for key, val in prev.items():
        for j in graph[key]:
            if j in curr:
                curr[j] += val
            else:
                curr[j] = val
    prev = curr

if 0 in prev:
    print(prev[0]%1000000007)
else:
    print(0)