N, M = map(int, input().split())
basket = [i+1 for i in range(N)]
for r in range(M):
    i, j = map(int, input().split())
    basket[(i-1):j] = basket[(i-1):j][::-1]
print(' '.join(map(str, basket)))