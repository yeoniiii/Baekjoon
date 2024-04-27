import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: x[0])
    num = 1
    min_interview = 100000
    for j in range(1, N):
        min_interview = min(min_interview, arr[j-1][1])
        if arr[j][1] < min_interview:
            num += 1
    print(num)            
               