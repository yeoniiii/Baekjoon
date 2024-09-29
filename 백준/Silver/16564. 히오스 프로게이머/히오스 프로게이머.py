import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
X = []
for _ in range(N):
    X.append(int(input()))
    
def check(T):
    s = 0
    for x in X:
        if x < T:
            s += T-x
    return s
    
l, r = min(X), max(X)+K
while l <= r:
    mid = (l+r)//2
    if check(mid) <= K:
        T = mid
        l = mid+1
    else:
        r = mid-1
print(T)