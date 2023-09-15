N = int(input())
arr = []
for i in range(2000):
    for j in range(1001):
        if 3*i + 5*j == N:
            arr.append(i+j)
if len(arr) == 0:
    print(-1)
else:
    print(min(arr))