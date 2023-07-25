N, B = map(int, input().split())

i = 0
while True:
    if N // B**i == 0: break
    i += 1

arr = [0]*i
for j in range(i):
    n, m = divmod(N, B**(i-j-1))
    if n < 10:
        arr[j] = n
    else:
        arr[j] = chr(n + 55)
    N = m
print(*arr, sep='')
    
