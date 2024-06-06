N, day = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

ans = []

if day == 1:
    ans.append(bg)
    ans.append(bb)
else:
    ans.append(gg)
    ans.append(gb)

for i in range(N-1):
    good = ans[0]*gg + ans[1]*bg
    bad = ans[0]*gb + ans[1]*bb
    ans[0] = good
    ans[1] = bad
 
for a in ans:
    print(round(a * 1000))