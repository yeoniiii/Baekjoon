import sys
N = int(sys.stdin.readline())
S = []

for _ in range(N):
    op = sys.stdin.readline().split()
    if op[0] == 'pop':
        if len(S) > 0: print(S.pop())
        else: print(-1)
    elif op[0] == 'size':
        print(len(S))
    elif op[0] == 'empty':
        print(int(len(S)==0))
    elif op[0] == 'top':
        if len(S) != 0:
            print(S[-1])
        else: print(-1)
    else: # push
        S.append(op[1])