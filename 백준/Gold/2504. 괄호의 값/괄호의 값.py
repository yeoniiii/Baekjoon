S = input()
N = len(S)
stack = []
bracket = {')':'(', ']':'['}
scores = {')':2, ']':3}

no = 0

for i in range(N):
    if no > 0:
        break
    if S[i] in bracket.values():
        stack.append(S[i])
    elif S[i] in bracket:
        s = 0
        match = 0
        while stack:
            if stack[-1] == bracket[S[i]]:
                stack.pop()
                match = 1
                break
            elif stack[-1] in bracket.values():
                no += 1
                break
            s += stack.pop()
        if match == 0:
            no += 1
        if s == 0:
            stack.append(scores[S[i]])
        else:
            stack.append(scores[S[i]] * s)

for s in stack:
    if s in bracket.values() or s in bracket:
        no += 1
if no > 0:
    print(0)
else:
    print(sum(stack))