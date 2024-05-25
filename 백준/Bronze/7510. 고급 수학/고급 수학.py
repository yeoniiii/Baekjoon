import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
for i in range(n):
    print(f"Scenario #{i+1}:")
    arr = sorted(list(map(int, input().split())))
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print("yes")
    else:
        print("no")
    print()