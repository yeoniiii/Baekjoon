w, h = map(int, input().split())
n, d = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))
lane = [a[0]]
for i in range(1, n):
    lane.append(a[i]-a[i-1])

if d == h:
    ans = p[-1]*w
    for i in range(n):
        ans += p[i]*lane[i]
    print(ans)
    
elif n == 1:
    ans = p[0]*(w+d)
    print(ans)

else:
    cases = []
    for i in range(n-1):
        if d < a[0]:
            cases.append(0)
            cases.append(1)
            break
        if a[i] == d:
            cases.append(i)
            break
        if a[i] < d < a[i+1]:
            cases.append(i)
            cases.append(i+1)
        
    if len(cases) == 1:
        ans = p[i+1]*w
        for k in range(cases[0]):
            ans += p[k]*lane
        print(ans)
    elif len(cases) == 2:
        i, j = cases
        ans_i, ans_j = p[i]*w, p[j]*w
        curr_lane = 0
        for k in range(i):
            ans_i += p[k]*lane[k]
            ans_j += p[k]*lane[k]
            curr_lane += lane[k]
        ans_i += p[i]*(d-curr_lane)
        ans_j += p[i]*lane[i] + p[i]*(curr_lane+lane[i]-d)
        
        print(min(ans_i, ans_j))