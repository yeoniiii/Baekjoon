W, H, N = map(int, input().split())
if N % 2 == 1:
    s = 0
    for i in range(1, N, 2):
        s += i
    print(s/N * H * 2)
else:
    s = 0
    for i in range(1, N//2):
        s += i
    print(s/N * H * 4)