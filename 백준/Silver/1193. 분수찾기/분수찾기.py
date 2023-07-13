X = int(input())

n = round((2*X)**0.5)
a = int(X - (n-1)*n/2)
b = int((n+1) - a)
if n % 2 != 0:
    save = a
    a = b
    b = save
print(a,"/", b, sep="")