T = int(input())
for t in range(T):
    arr = list(input().split())
    for a in arr:
        print(a[::-1], end=' ')
    print()