char = input()
ans = ''
for c in char:
    if c.isupper(): ans += c.lower()
    else: ans += c.upper()
print(ans)