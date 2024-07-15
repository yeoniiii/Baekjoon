import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for n in range(N):
    arr.append(int(input()))
arr.sort()
while True:
    if arr[-1] < arr[-2] + arr[-3]:
        print(arr[-1]+arr[-2]+arr[-3])
        break
    elif len(arr) > 3:
        arr.pop()
    else:
        print(-1)
        break