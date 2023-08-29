from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
L = deque()

N = int(input())
for _ in range(N):
    comm = input()
    if comm.split()[0] == "push_front":
        L.appendleft(int(comm.split()[1]))
    elif comm.split()[0] == "push_back":
        L.append(int(comm.split()[1]))
    elif comm == "pop_front":
        if len(L) > 0: print(L.popleft())
        else: print(-1)
    elif comm == "pop_back":
        if len(L) > 0: print(L.pop())
        else: print(-1)
    elif comm == "size":
        print(len(L))
    elif comm == "empty":
        print(int(len(L)==0))
    elif comm == "front":
        if len(L) > 0: print(L[0])
        else: print(-1)
    elif comm == "back":
        if len(L) > 0: print(L[-1])
        else: print(-1)