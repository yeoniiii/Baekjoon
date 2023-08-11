N = int(input())
div = sorted(list(map(int, input().split())))
if N % 2 == 0:
    print(div[0]*div[-1])
else:
    mid = int((N-1)/2)
    print(div[mid]**2)