N = int(input())
arr = []
for i in range(3):
    arr.append(input())
exist = 0
HJS = {}
num = [''] * 3
i = 0
while i < N:
    if arr[0][i] == arr[1][i] == arr[2][i]:
        i += 1
    elif arr[0][i] != arr[1][i] and arr[1][i] != arr[2][i] and arr[2][i] != arr[0][i]:
        exist = 1
        break
    elif arr[0][i] == arr[2][i] and arr[0][i] != arr[1][i]:
        break
    else:
        HJS[arr[0][i]] = 2
        HJS[arr[2][i]] = 4
        remain = 'HJS'.replace(arr[0][i], '').replace(arr[2][i], '')
        for r in [1, 3, 5]:
            for j in range(3):
                num[j] = arr[j]
                for k, v in HJS.items():
                    num[j] = num[j].replace(k, str(v))
                num[j] = num[j].replace(remain, str(r))
            if int(num[0]) < int(num[1]) < int(num[2]):
                exist = 1
                break
        break

if exist == 0:
    print('Hmm...')
elif exist == 1:
    print('HJS! HJS! HJS!')   