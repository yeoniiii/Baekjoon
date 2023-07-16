while True:
    arr = list(map(int, input().split()))
    arr.sort()
    arr_max = arr.copy()
    arr_max.remove(max(arr))
    if max(arr) >= sum(arr_max):
        if sum(arr) == 0: break
        else: print("Invalid")
    else:
        if len(set(arr)) == 1: print("Equilateral")
        elif len(set(arr)) == 2: print("Isosceles")
        else: print("Scalene")