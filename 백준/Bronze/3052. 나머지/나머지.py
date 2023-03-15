import sys
arr = list(map(int, sys.stdin.readlines()))
remain = []

for i in arr:
    remain.append(i%42)
print(len(set(remain)))