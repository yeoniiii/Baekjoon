import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = list(map(int, input().split()))

num = 0
start, end = 0, 1
s = A[start]

while True:
    if s < M:
        if end < N:
            s += A[end]
            end += 1
        else:
            break
    elif s == M:
        num += 1
        s -= A[start]
        start += 1
    else:
        s -= A[start]
        start += 1
    

print(num)