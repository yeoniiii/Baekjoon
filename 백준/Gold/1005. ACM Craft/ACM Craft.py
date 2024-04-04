import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

T = int(input())
for t in range(T):
    N, K = map(int, input().split()) # 건물 개수, 규칙 개수
    delay = list(map(int, input().split()))
    indegree = [0] * (N+1)
    graph = [[] for i in range(N+1)]
    
    for k in range(K):
        X, Y = map(int, input().split()) # X -> Y
        graph[X].append(Y)
        indegree[Y] += 1
      
    result = 0
    q = deque()
    dp = [0] * (N+1)
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = delay[i-1]
            
    W = int(input())
    while q:
        v = q.popleft()
        for i in graph[v]:
            indegree[i] -= 1
            dp[i] = max(dp[v]+delay[i-1], dp[i])
            if indegree[i] == 0:
                q.append(i)

    print(dp[W])