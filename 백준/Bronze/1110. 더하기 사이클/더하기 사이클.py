N = int(input())
t = 0
n = N
while True:
    t+=1
    a, b = divmod(n, 10)
    n = 10 * b + (a+b) % 10
    if n == N: break
print(t)