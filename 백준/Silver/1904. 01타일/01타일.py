N = int(input())
d = [0] * (N+1)
d[0] = 1
d[1] = 1

if 2 <= N+1:
    for i in range(2, N+1):
        d[i] = (d[i-2] + d[i-1]) % 15746
    
print(d[N])