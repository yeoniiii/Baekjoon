N, K = map(int, input().split())
arr = []
for k in range(1, K+1):
    arr.append(int(str(N*k)[::-1]))
print(max(arr))