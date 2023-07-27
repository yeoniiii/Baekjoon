import sys
N = int(input())

arr = [0]*10001
for _ in range(N):
    n = int(sys.stdin.readline())
    arr[n] += 1
for a in range(10001):
    if arr[a] > 0:
        for i in range(arr[a]):
            print(a)