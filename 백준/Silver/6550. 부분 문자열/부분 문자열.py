while True:
    try:
        s, t = input().split()
        t = list(t)
        ans = ''

        for i in range(len(s)):
            while t:
                if s[i] == t[0]:
                    ans += t.pop(0)
                    break
                t.pop(0)
        if ans == s:
            print('Yes')
        else:
            print('No')
    except:
        break