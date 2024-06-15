import sys
input = lambda: sys.stdin.readline().rstrip()

M, n = map(int, input().split())
pos = [0, 0]
d = 0 # 동0남1서2북3
out = 0

for i in range(n):
    command, direction = input().split()
    direction = int(direction)
    
    if command == 'MOVE':
        new_pos = [0, 0]
        if d == 0: # 동
            new_pos[0] = pos[0] + direction
            new_pos[1] = pos[1]
        elif d == 1: # 남
            new_pos[0] = pos[0]
            new_pos[1] = pos[1] - direction
        elif d == 2: # 서
            new_pos[0] = pos[0] - direction
            new_pos[1] = pos[1]
        else: # 북
            new_pos[0] = pos[0]
            new_pos[1] = pos[1] + direction
        if 0 <= new_pos[0] <= M and 0 <= new_pos[1] <= M:
            pos[0] = new_pos[0]
            pos[1] = new_pos[1]
        else:
            out = 1
    elif command == 'TURN':
        if direction == 0: # 왼쪽으로 90도 회전
            if d == 0:
                d = 3
            else:
                d -= 1
        else: # 오른쪽으로 90도 회전
            if d == 3:
                d = 0
            else:
                d += 1
if out == 1:
    print(-1)
else:
    print(*pos)