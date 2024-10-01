import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, Q = map(int, input().split())
back = deque()
forward = deque()
curr = 0

for _ in range(Q):
    task = input()
    if task == 'B':
        if back:
            forward.appendleft(curr)
            curr = back.pop()
    elif task == 'F':
        if forward:
            back.append(curr)
            curr = forward.popleft()
    elif task[0] == 'A':
        task, x = task.split(' ')
        forward = deque()
        if curr > 0:
            back.append(curr)
        curr = int(x)
    elif task == 'C':
        if back and len(set(back)) < len(back):
            new_back = [back[0]]
            for i in range(1, len(back)):
                if back[i] != new_back[-1]:
                    new_back.append(back[i])
            back = new_back[:]
print(curr)
if back:
    print(*reversed(back))
else:
    print(-1)
if forward:
    print(*forward)
else:
    print(-1)