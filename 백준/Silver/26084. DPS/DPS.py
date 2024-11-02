import sys
input = lambda: sys.stdin.readline().rstrip()

S = input()
d = {}
for s in S:
    d[s] = 0
    
N = int(input())
for n in range(N):
    handle = input()
    if handle[0] in d:
        d[handle[0]] += 1

if len(d) == 1:
    n = d[S[0]]
    print(n*(n-1)*(n-2)//3//2)
elif len(d) == 3:
    print(d[S[0]]*d[S[1]]*d[S[2]])
else:
    if S[0] == S[1]:
        n = d[S[0]]
        print(n*(n-1)//2*d[S[2]])
    elif S[1] == S[2]:
        n = d[S[1]]
        print(n*(n-1)//2*d[S[0]])
    else:
        n = d[S[0]]
        print(n*(n-1)//2*d[S[1]])