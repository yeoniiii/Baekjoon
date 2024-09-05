T = int(input())
for t in range(T):
    s, p = input().split()
    l = len(s)
    sec = 0
    s = s.replace(p, '')
    sec += (l-len(s))//len(p)
    sec += len(s)
    print(sec)