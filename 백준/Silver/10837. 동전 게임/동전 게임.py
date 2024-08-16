import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
C = int(input())
for c in range(C):
    M, N = map(int, input().split())
    if M == N:
        print(1)
    elif M < N:
        if N*2 - M - K <= 1:
            print(1)
        else:
            print(0)
    else:
        if M*2 - N - K <= 2:
            print(1)
        else:
            print(0)