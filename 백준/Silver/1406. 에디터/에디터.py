import sys
input = lambda: sys.stdin.readline().rstrip()

S_left = list(input())
S_right = []
M = int(input())

for i in range(M):
    command = input()
    if command[0] == 'L':
        if S_left:
            S_right.append(S_left.pop())
    elif command[0] == 'D':
        if S_right:
            S_left.append(S_right.pop())
    elif command[0] == 'B':
        if S_left:
            S_left.pop()
    elif command[0] == 'P':
        S_left.append(command[-1])
        
print(''.join(S_left+S_right[::-1]))