N = int(input())
num = 0

for i in range(N):
    wrd = [w for w in input()]
    ans = wrd.copy()
    for l in range(len(wrd)-1):
        if wrd[l] == wrd[l+1]: pass
        elif wrd[l] in wrd[l+1:]:
            ans.remove(wrd[l])
    if ans == wrd: num += 1
print(num)