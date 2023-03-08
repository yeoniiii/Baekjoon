a = int(input())
b = int(input())

c, d = divmod(b, 100)
d, e = divmod(d, 10)

print(a*e)
print(a*d)
print(a*c)
print(a*b)