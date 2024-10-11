import sys
input = lambda: sys.stdin.readline().rstrip()

available = True

N = int(input())
for n in range(N):
    X, Y = map(int, input().split())
    arr = []
    for x in range(X):
        arr.append(list(map(int, input().split())))
    if n == 0:
        prev_arr = arr
    elif len(prev_arr[0]) != X:
        available = False
        break
    else:
        new_arr = [[0] * Y for _ in range(len(prev_arr))]
        for z in range(len(prev_arr)):
            for y in range(Y):
                for x in range(X):
                    new_arr[z][y] += prev_arr[z][x] * arr[x][y]
        prev_arr = new_arr
    
if available:
    ans = 0
    for i in range(len(prev_arr)):
        ans += sum(prev_arr[i]) % 1000000007
    print(ans % 1000000007)
else:
    print(-1)        