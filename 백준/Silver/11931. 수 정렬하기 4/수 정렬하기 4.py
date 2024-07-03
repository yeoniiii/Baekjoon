import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
print(*sorted(arr, reverse=True), end='\n')