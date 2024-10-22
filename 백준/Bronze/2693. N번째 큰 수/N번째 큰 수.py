T = int(input())
for t in range(T):
    A = sorted(list(map(int, input().split())))
    print(A[-3])