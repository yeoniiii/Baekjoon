bal = {')':'(', ']':'['}

while True:
    char = input()
    stack = []
    if char == '.': break
        
    for i in char:
        a = 0
        if i in ['(', '[']: # 열린 괄호
            stack.append(i)
        elif i in bal: # 닫힌 괄호
            if len(stack) != 0 and stack[-1] == bal[i]:
                stack.pop()
            else: 
                a += 1
                print("no")
                break
    if len(stack) == 0 and a==0: print("yes")
    elif len(stack) > 0 and a ==0: print("no")