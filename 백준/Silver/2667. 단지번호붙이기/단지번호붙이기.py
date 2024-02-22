N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))
    
def dfs(x, y):
    global num

    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        num += 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

ans =  []
for i in range(N):
    for j in range(N):
        num = 0
        if dfs(i, j) == True:
            ans.append(num)

print(len(ans))
print('\n'.join(map(str, sorted(ans))))