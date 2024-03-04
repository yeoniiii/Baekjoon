import sys
input = lambda: sys.stdin.readline().rstrip()

M = int(input())
S = set()

for i in range(M):
    inp = input()
    if inp == 'all':
        S = set(range(1, 21))
    elif inp == 'empty':
        S = set()
    else:
        c, n = inp.split()
        n = int(n)
        if c == 'add':
            S.add(n)
        elif c == 'remove':
            if int(n) in S:
                S.remove(n)
        elif c == 'check':
            print(int(int(n) in S))
        elif c == 'toggle':
            if int(n) in S:
                S.remove(n)
            else:
                S.add(n)