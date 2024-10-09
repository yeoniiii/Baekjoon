N, M = map(int, input().split())
board = [-1]
for n in range(N):
    board.append(int(input()))
pos = 1
cnt = 0
for m in range(M):
    pos += int(input())
    cnt += 1
    if pos >= N:
        break
    pos += board[pos]
    if pos >= N:
        break
print(cnt)