N = int(input())
arr = sorted(list(map(int, input().split())))
m = 0

for i in range(N):
    m += arr[i] * (N-i)

print(m)