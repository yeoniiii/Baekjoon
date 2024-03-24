import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
q = deque()

for i in range(N):
    com = input()
    if len(com) > 1:
        c, x = map(int, com.split())
        if c == 1:
            q.appendleft(x)
        if c == 2:
            q.append(x)
    else:
        c = int(com)
        if c == 3:
            if q:
                print(q.popleft())
            else:
                print(-1)
        if c == 4:
            if q:
                print(q.pop())
            else:
                print(-1)
        if c == 5:
            print(len(q))
        if c == 6:
            print(int(len(q)==0))
        if c == 7:
            if q:
                print(q[0])
            else:
                print(-1)
        if c == 8:
            if q:
                print(q[-1])
            else:
                print(-1)