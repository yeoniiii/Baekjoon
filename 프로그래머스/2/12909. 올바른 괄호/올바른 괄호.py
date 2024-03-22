def solution(s):
    answer = True
    stack = []
    for op in s:
        if op == '(':
            stack.append(op)
        elif len(stack) > 0:
            while stack[-1] != '(':
                stack.pop()
            if stack[-1] == '(':
                stack.pop()
        else:
                return False
    if len(stack) > 0:
        return False
    return True