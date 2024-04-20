stack = []
inp = input()
num, cnt = 0, 0
past = ''

for i in inp:
    if i == '(':
        stack.append(i)
        if past == '(':
            num += 1
    else:
        stack.pop()
        if past == '(':
            cnt += num
        else:
            cnt += 1
            num -= 1
    past = i
    
print(cnt)