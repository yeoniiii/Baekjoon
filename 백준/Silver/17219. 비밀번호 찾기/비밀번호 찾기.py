import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
d = {}

for i in range(N):
    link, password = input().split()
    d[link] = password
for i in range(M):
    link = input()
    print(d[link])