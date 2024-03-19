N = int(input())
x = input()
ops = {'*':1, '/':2, '+':2, '-':2}
alp = dict()
for i in range(N):
    alp[chr(ord('A')+i)] = int(input())
    
stack = []

for i in x:
    if i in ops:
        if len(stack) >= 2:
            x = stack.pop()
            y = stack.pop()
            if i == '*':
                stack.append(y*x)
            elif i == '/':
                stack.append(y/x)
            elif i == '+':
                stack.append(y+x)
            elif i == '-':
                stack.append(y-x)

    elif i in alp:
        stack.append(alp[i])
        
print('{:.2f}'.format(stack[0]))