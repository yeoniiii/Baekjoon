x, n = int(input()), int(input())
s = 0
    
for i in range(n) :
    a, b = map(int, input().split())
    s += a*b

print('Yes' if s==x else 'No')