from collections import deque

A, B = map(int, input().split())

def bfs(x):
    arr = []
    q = deque()
    q.append((x*2, 1))
    q.append((int(str(x)+'1'), 1))
    while q:
        v, cnt = q.popleft()
        if v == B:
            return cnt + 1
        elif v < B:
            q.append((v*2, cnt+1))
            q.append((int(str(v)+'1'), cnt+1))
    return -1
    
print(bfs(A))