import sys
input = lambda: sys.stdin.readline().rstrip()
t = 1

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    print('Triangle #' + str(t))
    if a == -1:
        l = (c**2 - b**2) ** (1/2)
        if c**2 - b**2 > 0 and l + b > c:
            print(f'a = {l:.3f}')
        else:
            print('Impossible.')
    elif b == -1:
        l = (c**2 - a**2) ** (1/2)
        if c**2 - a**2 > 0 and a + l > c:
            print(f'b = {l:.3f}')
        else:
            print('Impossible.')
    elif c == -1:
        l = (a**2 + b**2) ** (1/2)
        if a**2 + b**2 > 0 and a + b > l:
            print(f'c = {l:.3f}')
        else:
            print('Impossible.')
    
    print()
    t += 1