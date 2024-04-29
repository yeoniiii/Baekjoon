N, r, c = map(int, input().split())
dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]

def Z(N, r, c, cnt):
    if N == 1:
        for i in range(4):
            if dr[i] == r and dc[i] == c:
                return cnt + i

    cut = 2**(N-1)
    if r < cut and c < cut:
        return Z(N-1, r, c, cnt+4**(N-1)*0)
    elif r < cut and c >= cut:
        return Z(N-1, r, c%cut, cnt+4**(N-1)*1)
    elif r >= cut and c < cut:
        return Z(N-1, r%cut, c, cnt+4**(N-1)*2)
    elif r >= cut and c >= cut:
        return Z(N-1, r%cut, c%cut, cnt+4**(N-1)*3)

print(Z(N, r, c, 0))