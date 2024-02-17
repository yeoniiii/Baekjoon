N = int(input())
arr = list(map(int, input().split()))
arr_save = []
order = 1

while len(arr) > 0:
    if arr[0] == order:
        arr.pop(0)
        order += 1
    else:
        arr_save.append(arr.pop(0))
        
    while len(arr_save) > 0:
        if arr_save[-1] == order:
            arr_save.pop()
            order += 1
        else:
            break
            
if len(arr) == 0 and order == N+1:
    print('Nice')
else:
    print('Sad')