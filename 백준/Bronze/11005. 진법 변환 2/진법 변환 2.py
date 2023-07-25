N, B = map(int, input().split())

i = 0
while True:
    if N // B**i == 0: break
    i += 1

ans = ''
for j in range(i):
    n, m = divmod(N, B**(i-j-1))
    if n < 10:
        ans += str(n)
    else:
        ans += chr(n + 55)
    N = m
print(ans)
    
