import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
dict = {}

for n in range(N):
    name = input()
    dict[n+1] = name
    dict[name] = n+1
for m in range(M):
    q = input()
    if q.isdigit():
        print(dict[int(q)])
    else:
        print(dict[q])