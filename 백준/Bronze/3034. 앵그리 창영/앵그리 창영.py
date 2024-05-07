N, W, H = map(int, input().split())
for i in range(N):
    x = int(input())
    if x**2 <= W**2 + H**2:
        print("DA")
    else:
        print("NE")