N = int(input())

def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-1)*n
    
nfac = str(factorial(N))
for i in range(len(nfac)):
    if nfac[len(nfac) - i - 1] != '0':
        print(i)
        break