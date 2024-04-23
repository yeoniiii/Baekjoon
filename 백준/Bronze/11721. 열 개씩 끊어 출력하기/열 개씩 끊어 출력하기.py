arr = list(input())
i = 0
while True:
    if i+10 < len(arr):
        print(''.join(arr[i:(i+10)]))
    else:
        print(''.join(arr[i:]))
        break
    i += 10