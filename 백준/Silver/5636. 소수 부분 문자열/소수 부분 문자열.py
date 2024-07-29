def prime(n):
    arr = [1] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i+i, n+1, i):
                arr[j] = 0
    p = [i for i in range(2, n+1) if arr[i]]
    return p

while True:
    S = input()
    if S == '0':
        break
    p = prime(10**5)
    ans = 1
    for n in p:
        if str(n) in S:
            ans = n
    print(ans)