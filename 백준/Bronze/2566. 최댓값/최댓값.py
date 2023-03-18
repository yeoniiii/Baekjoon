arr = [list(map(int, input().split())) for _ in range(9)]

row_max = []
col_max_ind = []

for i in range(9):
    row_max.append(max(arr[i]))
    col_max_ind.append(arr[i].index(max(arr[i])))
print(max(row_max))

row_n = row_max.index(max(row_max))
col_n = col_max_ind[row_n]

print(row_n+1, col_n+1)