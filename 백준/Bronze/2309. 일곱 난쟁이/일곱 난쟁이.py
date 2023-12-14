arr = []
for i in range(9):
    arr.append(int(input()))
    
for a in range(8):
    for b in range(a+1, 9):
        if sum(arr) - arr[a] - arr[b] == 100:
            arr.remove(arr[b])
            arr.remove(arr[a])
            break
    if len(arr) == 7:
        break
sarr = sorted(arr)
for i in range(7):
    print(sarr[i])