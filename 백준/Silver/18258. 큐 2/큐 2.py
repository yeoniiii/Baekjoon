import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
queue = deque([])

for _ in range(N):
    op = input()
    if op == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else: print(-1)
    elif op == 'size':
        print(len(queue))
    elif op == 'empty':
        print(int(len(queue)==0))
    elif op == 'front':
        if len(queue) != 0:
            print(queue[0])
        else: print(-1)
    elif op == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else: print(-1)
    else: # push
        queue.append(int(op.split()[1]))