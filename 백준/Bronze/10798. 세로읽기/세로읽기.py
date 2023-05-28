arr = []
for i in range(5):
    arr.append([w for w in input()])

len_arr = []
for i in range(len(arr)):
    len_arr.append(len(arr[i]))
n = max(len_arr)

for i in range(len(arr)):
    if len(arr[i])<n : 
        for j in range(n-len(arr[i])):
            arr[i].append('')

ans = []
for c in range(n):
    for r in range(len(arr)):
        if arr[r][c]=='': pass
        ans.append(arr[r][c])
print(''.join(ans))