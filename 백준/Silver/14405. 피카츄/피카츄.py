S = input()
can = ["pi", "ka", "chu"]
for c in can:
    S = S.replace(c, ' ')
if S == ' '*len(S):
    print("YES")
else:
    print("NO")