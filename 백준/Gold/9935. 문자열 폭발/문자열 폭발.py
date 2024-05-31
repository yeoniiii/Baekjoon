S = input()
N = len(S)
bomb = list(input())
M = len(bomb)
q = []

for s in S:
    if s != bomb[-1]:
        q.append(s)
    else:
        if M > 1:
            if q[-M+1:] == bomb[:-1]:
                for i in range(M-1):
                    q.pop()
            else:
                q.append(s)
if q:
    print(*q, sep='')
else:
    print('FRULA')