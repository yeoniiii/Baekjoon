from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
q = deque()

for _ in range(N):
    comm = input()
    if comm == "pop":
        if len(q) > 0: print(q.popleft())
        else: print(-1)
    elif comm == "size":
        print(len(q))
    elif comm == "empty":
        print(int(len(q)==0))
    elif comm == "front":
        if len(q) > 0: print(q[0])
        else: print(-1)
    elif comm == "back":
        if len(q) > 0: print(q[-1])
        else: print(-1)
    else:
        q.append(int(comm.split()[-1]))