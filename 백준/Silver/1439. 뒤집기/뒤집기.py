S = input()
cnt = 0

past = S[0]
for s in S[1:]:
    if s != past:
        cnt += 1
        past = s
if (cnt / 2) % 1 < 0.5:
    print(cnt//2)
else:
    print(cnt//2+1)