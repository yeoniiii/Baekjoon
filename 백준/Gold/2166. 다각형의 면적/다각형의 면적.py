N = int(input())
xs, ys = [], []
for n in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
xs.append(xs[0])
ys.append(ys[0])
ans = 0
for i in range(N):
    ans += xs[i] * ys[i+1]
for i in range(N, 0, -1):
    ans -= xs[i] * ys[i-1]
    
print(round(abs(ans)/2, 1))