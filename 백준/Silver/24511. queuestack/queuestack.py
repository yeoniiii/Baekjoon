import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
QS = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

q = deque()
for i in range(len(QS)):
    if QS[i] == 0: # 큐
        q.append(B[i])
    
for c in C:
    q.appendleft(c)

for i in range(M):
    l = len(q)
    print(q[l-i-1], end=' ')