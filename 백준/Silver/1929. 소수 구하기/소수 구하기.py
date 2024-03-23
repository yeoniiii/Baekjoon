M, N = map(int, input().split())

def prime(N):
    if N <= 1:
        return False
    else:
        for i in range(2, int(N**(1/2))+1):
            if N % i == 0:
                return False
        return True

for i in range(M, N+1):
    if prime(i):
        print(i)