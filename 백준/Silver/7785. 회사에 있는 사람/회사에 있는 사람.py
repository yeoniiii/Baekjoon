import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = set()

for i in range(n):
    log = input().split()
    if log[1] == 'enter':
        arr.add(log[0])
    else:
        arr.remove(log[0])

arr = list(arr)
arr.sort(reverse=True)
for nm in arr:
    print(nm)