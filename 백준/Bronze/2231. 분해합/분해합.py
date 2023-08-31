import sys

N = int(sys.stdin.readline())
ans = 0

for i in range(1, N+1):
    nums = list(map(int, str(i)))
    s = i + sum(nums)
    if s == N: 
        ans = i
        break
print(ans)