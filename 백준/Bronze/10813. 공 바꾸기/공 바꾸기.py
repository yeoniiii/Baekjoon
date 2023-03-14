N, M = map(int, input().split())

arr = [i+1 for i in range(N)]

for m in range(M):
    i, j = map(int, input().split())
    save = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = save
print(' '.join(list(map(str, arr))))
    