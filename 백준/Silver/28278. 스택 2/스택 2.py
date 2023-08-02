import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

stack = []
for _ in range(N):
    op = input()
    if op == '2':
        if len(stack) != 0:
            popnum = stack.pop()
            print(popnum)
        else: print(-1)
    elif op == '3':
        print(len(stack))
    elif op == '4':
        print(int(len(stack)==0))
    elif op == '5':
        if len(stack) != 0:
            print(int(stack[-1]))
        else: print(-1)
    else: # 1 X
        stack.append(int(op.split()[1]))