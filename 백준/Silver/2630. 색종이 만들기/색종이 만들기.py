import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

r = [0, 0, 1, 1]
c = [0, 1, 0, 1]

ans = [0, 0]
    
def paper(sr, sc, pos, size):
    sr, sc = sr + r[pos] * size, sc + c[pos] * size
    er, ec = sr + size, sc + size
    color = arr[sr][sc]
    cnt = 0
    
    for i in range(sr, er):
        for j in range(sc, ec):
            if arr[i][j] == color:
                cnt += 1

    if cnt == size**2:
        ans[color] += 1
        return

    for i in range(4):
        paper(sr, sc, i, size//2)
    
paper(0, 0, 0, N)
print('\n'.join(map(str, ans)))