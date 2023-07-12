M = int(input())
N = int(input())

arr = []
for i in range(M, N+1):
    num = 0
    for j in range(1, i+1):
        if i % j == 0:
            num += 1
    if num == 2:
        arr.append(i)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else : print(-1)