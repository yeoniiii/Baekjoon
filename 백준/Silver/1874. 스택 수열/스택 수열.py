n = int(input())
a, cnt, op, stack = 0, 1, [], []

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        print("NO")
        a += 1
        break

if a == 0:
    print(*op, sep='\n')
    