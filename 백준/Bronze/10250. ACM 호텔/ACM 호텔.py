T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    arr = [0]*(H*W)
    for i in range(len(arr)):
        a, b = divmod(i, H)
        arr[i] = (b+1)*100 + (a+1)
    print(arr[N-1])       
        