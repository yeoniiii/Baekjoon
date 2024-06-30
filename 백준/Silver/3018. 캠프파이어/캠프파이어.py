import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
E = int(input())
know = {}
for i in range(1, N+1):
    know[i] = 0
for i in range(E):
    arr = list(map(int, input().split()))
    K = arr.pop(0)
    arr.sort()
    for a in arr:
        if arr[0] == 1:
            know[a] += 1
        else:
            know[a] = max(know.values())

max_num = max(know.values())
for key, value in know.items():
    if value == max_num:
        print(key)