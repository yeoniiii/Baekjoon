from collections import deque
N = int(input())
q = deque()
for i in range(1, N+1):
    q.append(i)
step = 1
while len(q) > 1:
    popnum = (step**3)%(len(q))
    if popnum == 0:
        popnum += len(q)
    for s in range(popnum-1):
        q.append(q.popleft())
    q.popleft()
    step += 1
print(q[0])