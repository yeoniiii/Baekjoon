def Fibonacci(n):
    ans = 0
    if n <= 1:
        return n
    else:
        ans = Fibonacci(n-2) + Fibonacci(n-1)
    return(ans)

n= int(input())
print(Fibonacci(n))