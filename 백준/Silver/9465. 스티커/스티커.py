def sticker(N):
    arr = []
    for i in range(2):
        arr.append(list(map(int, input().split())))

    d = [[0] * N for _ in range(2)]
    
    d[0][0] = arr[0][0]
    d[1][0] = arr[1][0]
    
    if N >= 2:
        d[0][1] = d[1][0] + arr[0][1]
        d[1][1] = d[0][0] + arr[1][1]

    if N >= 3:
        for i in range(2, N):
            d[0][i] = max(d[1][i-1], d[1][i-2]) + arr[0][i]
            d[1][i] = max(d[0][i-1], d[0][i-2]) + arr[1][i]
    
    return max(d[0][-1], d[1][-1])

T = int(input())
for t in range(T):
    n = int(input())
    print(sticker(n))