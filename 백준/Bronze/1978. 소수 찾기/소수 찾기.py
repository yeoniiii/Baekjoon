N = int(input())
num = input().split()

prime = 0
for i in range(N):
    n = int(num[i])
    div = 0
    for j in range(1, n+1):
        if n % j == 0:
            div += 1
    if div == 2:
        prime += 1
print(prime)