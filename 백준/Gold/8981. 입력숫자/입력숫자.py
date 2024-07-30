N = int(input())
print(N)

Y = list(map(int, input().split()))
X = [0] * N

i, j, cnt = 0, 0, 0
X[i] = Y[j]
j += 1
i += X[i]

while j < N:
    while X[i%N] != 0:
        i += 1
    X[i%N] = Y[j]
    j += 1
    i += X[i%N]
print(*X)