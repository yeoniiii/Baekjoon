import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())

for _ in range(T):
    a = 0
    ps = input()
    stack = []
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        else: 
            if len(stack) != 0:
                stack.pop()
            else:
                a += 1
                print("NO")
                break
    if len(stack) == 0 and a == 0: print("YES")
    elif len(stack) > 0 and a == 0: print("NO")