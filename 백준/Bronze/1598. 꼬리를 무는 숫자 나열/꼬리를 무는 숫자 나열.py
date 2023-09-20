a, b = map(int, input().split())
def point(n):
    if n % 4 == 0:
        return [4, n//4 - 1]
    else:
        return [n % 4, n//4]
print(abs(point(a)[0] - point(b)[0]) + abs(point(a)[1] - point(b)[1]))