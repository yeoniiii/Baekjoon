from collections import deque

N, K = map(int, input().split())
answer = list(map(int, input().split()))
q = list(map(int, input().split()))

def pull(q, p):
    front, back = q[:p], deque(q[p:])
    back.popleft()
    back.append(0)
    return front + list(back)

def push(q, p):
    front, back = q[:p], deque(q[p:])
    back.pop()
    back.appendleft(0)
    return front + list(back)

result = 0

def dfs(v, q):
    global result
    num = 0
    for i in range(N):
        if answer[i] == q[i]:
            num += 1
    
    if num > result:
        result = num
        
    if v < K:
        for i in range(N):
            dfs(v+1, pull(q, i))
            dfs(v+1, push(q, i))
            
dfs(0, q)
print(result)