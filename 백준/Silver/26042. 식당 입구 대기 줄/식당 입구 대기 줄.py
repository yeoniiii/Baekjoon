import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = []
maxs = [0, 0]
for i in range(n):
    info = input()
    if info[0] == '1':
        arr.append(int(info.split()[1]))
        if maxs[0] < len(arr):
            maxs[0] = len(arr)
            maxs[1] = arr[-1]
        elif maxs[0] == len(arr):
            maxs[1] = min(maxs[1], arr[-1])
    elif info[0] == '2':
        arr.pop(0)

print(*maxs)