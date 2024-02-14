import sys
input = lambda: sys.stdin.readline().rstrip()
time = []

N = int(input())
for i in range(N):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x:(x[1], x[0]))

cnt, t, i = 1, 0, 1
while t+i < N:
    if time[t][1] <= time[t+i][0]:
        t += i
        cnt += 1
        i = 1
    else:
        i += 1
            
print(cnt)