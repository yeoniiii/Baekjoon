N, M = map(int, input().split()) # 바구니 개수, 공 넣는 횟수

arr = [0 for i in range(N)]
for m in range(M):
    i, j, k = map(int, input().split())
    arr[i-1:j] = [k for r in range(j-i+1)]
print(*arr)