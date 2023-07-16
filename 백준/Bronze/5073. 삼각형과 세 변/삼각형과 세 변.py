while True:
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[2] >= arr[0] + arr[1]:
        if sum(arr) == 0: break
        else: print("Invalid")
    else:
        if len(set(arr)) == 1: print("Equilateral")
        elif len(set(arr)) == 2: print("Isosceles")
        else: print("Scalene")