from collections import deque

A, B = map(int, input().split())
arr = []

def bfs(x):
    arr = []
    q = deque()
    q.append((x*2, 1))
    q.append((int(str(x)+'1'), 1))
    while q:
        v, cnt = q.popleft()
        if v == B:
            arr.append(cnt)
        elif v < B:
            cnt += 1
            q.append((v*2, cnt))
            q.append((int(str(v)+'1'), cnt))
    return arr
    
arr = bfs(A)
if len(arr) > 0:
    print(min(arr)+1)
else:
    print(-1)