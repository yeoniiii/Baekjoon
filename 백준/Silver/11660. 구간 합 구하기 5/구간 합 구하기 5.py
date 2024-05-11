import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    
cumsum = [[0] for i in range(N)]
for i in range(N):
    for j in range(N):
        cumsum[i].append(cumsum[i][j] + graph[i][j])
    
def SectionSum(x1, y1, x2, y2):
    s = 0
    for i in range(x1-1, x2):
        s += cumsum[i][y2] - cumsum[i][y1-1]
    return s

for j in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(SectionSum(x1, y1, x2, y2))