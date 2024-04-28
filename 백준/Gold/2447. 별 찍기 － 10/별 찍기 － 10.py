def star(N):
    if N == 1:
        return ['*'*3, '* *', '*'*3]

    stars = star(N-1)
    arr = []

    for s in stars:
        arr.append(s*3)
    for s in stars:
        arr.append(s+' '*3**(N-1)+s)
    for s in stars:
        arr.append(s*3)

    return arr

N = int(input())
k = 0
while N % 3 == 0:
    N //= 3
    k += 1
print('\n'.join(star(k)))