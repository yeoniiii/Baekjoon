import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
home = []
for i in range(N):
    home.append(int(input()))
home.sort()
    
start, end = 1, max(home) - min(home)
while start <= end:
    router = [min(home)]
    mid = (start + end) // 2
    for h in home:
        if h - router[-1] >= mid:
            router.append(h)
    cnt = len(router)
    if cnt >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)