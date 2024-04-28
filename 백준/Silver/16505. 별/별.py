N = int(input())
def star(N):
    if N == 0:
        return ['*']

    stars = star(N-1)
    arr = []

    for i, s in enumerate(stars):
        arr.append(s + ' '*i + s)
    for s in stars:
        arr.append(s)

    return arr

print('\n'.join(star(N)))