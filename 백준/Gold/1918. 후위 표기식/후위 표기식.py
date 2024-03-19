x = input()
ops = {'*':1, '/':1, '+':2, '-':2, '(':3}

stack = []
ans = ''

for i in x:
    if i in ops:
        if len(stack) == 0:
            stack.append(i)
        else:
            if ops[i] < ops[stack[-1]] or i == '(':
                stack.append(i)
            else:
                while len(stack) > 0:
                    if ops[stack[-1]] <= ops[i]:
                        ans += stack.pop()
                    else:
                        break
                stack.append(i)

    elif i == ')':
        while stack[-1] != '(':
            ans += stack.pop()
        stack.pop() # (

    else: # 문자열
        ans += i
    
while len(stack) > 0:
    ans += stack.pop()

print(ans)