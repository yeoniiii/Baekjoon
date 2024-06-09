from itertools import combinations

cards = input().split(',')
arr = []

for c1, c2 in combinations(cards, 2):
    arr.append([c1+c2])
    
for i in range(len(arr)):
    n1, c1, n2, c2 = arr[i][0]
    
    if abs(ord(n1) - ord(n2)) == 1 or n1+n2 in ['9a', 'a9', '1f', 'f1']:
        arr[i].append(1)
    elif n1 == n2:
        arr[i].append(2)
    else:
        arr[i].append(3)
    
    if c1 == c2:
        arr[i].append(1)
    else:
        arr[i].append(2)

    arr[i].append(max(ord(n1), ord(n2)))
    arr[i].append(min(ord(n1), ord(n2)))
    
    if ord(n1) > ord(n2):
        if c1 == 'b':
            arr[i].append(1)
        else:
            arr[i].append(0)
    else:
        if c2 == 'b':
            arr[i].append(1)
        else:
            arr[i].append(0)
    
arr.sort(key = lambda x: (x[1], x[2], -x[3], -x[4], -x[5]))

for i in range(len(arr)):
    print(arr[i][0])