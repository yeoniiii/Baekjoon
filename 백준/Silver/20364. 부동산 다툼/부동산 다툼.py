import sys
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
get = [0] * (N+1)

def check(end):
    if end == 1:
        return no
    if get[end] == 1:
        no.append(end)
    check(end//2)
        
for i in range(Q):
    duck = int(input())
    no = []
    check(duck)
    if not no:
        get[duck] = 1
        print(0)
    else:
        print(no[-1])