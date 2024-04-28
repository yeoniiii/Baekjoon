def star(N):
    if N == 0:
        return ['  *  ', ' * * ', '*'*5]

    stars = star(N-1)
    arr = []

    for s in stars:
        arr.append(' '*3*2**(N-1) +s+ ' '*3*2**(N-1))
    for s in stars:
        arr.append(s+' '+s)

    return arr

N = int(input())
N //= 3
k = 0
while N % 2 == 0:
    N //= 2
    k += 1
print('\n'.join(star(k)))