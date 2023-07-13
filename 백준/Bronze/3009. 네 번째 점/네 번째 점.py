x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def one(a, b, c):
    if a == b: return(c)
    elif a == c: return(b)
    else : return(a)
        
print(one(x1, x2, x3), one(y1, y2, y3))