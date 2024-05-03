import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ranks = deque(arr)
    docs = deque([i for i in range(N)])
    t = 0

    while ranks:
        r = ranks.popleft()
        d = docs.popleft()
        if len(ranks) == 0 or r >= max(ranks):
            t += 1
            if d == M:
                print(t)
                break
        else:
            ranks.append(r)
            docs.append(d)