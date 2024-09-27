from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    num = deque([i for i in range(len(priorities))])
    t = 1
    while q:
        x = q.popleft()
        if len(q) > 0 and x < max(q):
            q.append(x)
            num.append(num.popleft())
        else:
            if num.popleft() == location:
                return t
            t += 1