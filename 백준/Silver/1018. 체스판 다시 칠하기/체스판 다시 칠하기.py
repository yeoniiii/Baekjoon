import sys
input = lambda: sys.stdin.readline().rstrip()
board = []
result = []

N, M = map(int, input().split())
for _ in range(N):
    board.append(input())

for n in range(N-7):
    for m in range(M-7):
        b = 0
        w = 0
        for i in range(n, n+8):
            for j in range(m, m+8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'B': b += 1
                    if board[i][j] != 'W': w += 1
                else:
                    if board[i][j] != 'W': b += 1
                    if board[i][j] != 'B': w += 1
        result.append(b)
        result.append(w)
print(min(result))