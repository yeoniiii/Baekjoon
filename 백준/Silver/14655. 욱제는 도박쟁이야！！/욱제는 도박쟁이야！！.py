N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def calculate_sum(arr):
    s = 0
    for a in arr:
        if a < 0:
            s -= a
        else:
            s += a
    return s

print(calculate_sum(arr1)+calculate_sum(arr2))