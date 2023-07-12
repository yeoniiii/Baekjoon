N = int(input())

if N == 1 : print()
else:
    for i in range(2, N+1):
        while True:
            if N % i != 0 : break
            N = N // i
            print(i)