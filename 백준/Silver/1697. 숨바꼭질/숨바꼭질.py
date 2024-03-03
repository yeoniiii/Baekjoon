from collections import deque

N, K = map(int, input().split())
sec = [0] * 100001

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        v = q.popleft()
        if v == K:
            return sec[v]
        else:
            for i in [v-1, v+1, v*2]:
                if 0<=i<=100000 and sec[i] == 0:
                    sec[i] = sec[v] + 1
                    q.append(i)
    return sec[v]

print(bfs(N))