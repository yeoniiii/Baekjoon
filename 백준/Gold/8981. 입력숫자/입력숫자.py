N = int(input())
print(N)

Y = list(map(int, input().split()))
X = [0] * N

i, j, cnt = 0, 0, 0
X[i], Y[j] = Y[j], 0
j += 1
i += X[i]

while j < N:
    while X[i] != 0:
        i = (i + 1) % N
    X[i], Y[j] = Y[j], 0
    j += 1
    i = (i + X[i]) % N
print(*X)