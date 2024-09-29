from collections import deque

N, S, D, F, B, K = map(int, input().split())
if K == 0:
    l = []
else:
    l = list(map(int, input().split()))
    
building = [0] * (N+1)
for police in l:
    building[police] += 1
q = deque()

def bfs(S):
    cnt = 0
    q.append((S, cnt))
    while q:
        v, cnt = q.popleft()
        if building[v] == 1:
            continue
        building[v] += 1
        if v == D:
            return cnt
        if v+F <= N and v+F not in l:
            q.append((v+F, cnt+1))
        if v-B >= 1 and v-B not in l:
            q.append((v-B, cnt+1))
    return 'BUG FOUND'
            
print(bfs(S))