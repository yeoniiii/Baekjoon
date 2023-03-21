N, M = map(int, input().split())
basket = [i+1 for i in range(N)]
for r in range(M):
    i, j = map(int, input().split())
    select = basket[(i-1):j]
    select.reverse()
    basket[(i-1):j] = select
print(' '.join(map(str, basket)))