def canto(N):
    arr = ['-'] * 3**N

    if N == 0:
        return arr

    a, b = 3**(N-1), 3**(N-1)*2
    arr[a:b] = ' ' * 3**(N-1)
    
    if N == 1:
        return arr
    else:
        arr[:a] = canto(N-1)
        arr[b:] = canto(N-1)
        return arr

while True:
    try:
        N = int(input())
        print(*canto(N), sep='')
    except:
        break