N = int(input())
ans = 0
while N:
    s = str(N)
    ans += s.count("1")
    N = int("0" + s.replace("1", ""))
    if N:
        N -= 1
        ans += 1
print(ans)