L = int(input())
command = input()
x, y = 0, 0
S = set()
S.add(str(x)+','+str(y))
for c in command:
    if c == 'S':
        y -= 1
    elif c == 'N':
        y += 1
    elif c == 'E':
        x += 1
    elif c == 'W':
        x -= 1
    S.add(str(x)+','+str(y))
print(len(S))