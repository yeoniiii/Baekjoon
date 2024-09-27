import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
W = min(N, M)
arr = []
for n in range(N):
    arr.append(list(input()))

find = False
while not find:
    if W == 1:
        break
    for i in range(N-W+1):
        for j in range(M-W+1):
            if arr[i][j] == arr[i+W-1][j] == arr[i][j+W-1] == arr[i+W-1][j+W-1]:
                find = True
                break
        if find:
            break
    if not find:
        W -= 1
print(W**2)