arr = input().split('-')
ans = sum(list(map(int, arr[0].split('+'))))
for i in arr[1:]:
    ans -= sum(list(map(int, i.split('+'))))
print(ans)