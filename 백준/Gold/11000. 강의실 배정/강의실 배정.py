import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N = int(input())
s = []

for i in range(N):
    S, T = map(int, input().split())
    s.append((S, T))

s.sort()
q = [s[0][1]] # 큐에 가장 먼저 시작하는 회의실의 종료 시간을 넣음
    
for i in range(1, N):
    if s[i][0] < q[0]:
        heapq.heappush(q, s[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, s[i][1])

print(len(q))