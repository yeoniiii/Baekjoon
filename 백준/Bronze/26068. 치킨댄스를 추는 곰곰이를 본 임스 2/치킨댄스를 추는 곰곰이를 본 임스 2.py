import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
cnt = 0
for i in range(N):
    D, day = input().split('-')
    if int(day) <= 90:
        cnt += 1
print(cnt)