a, b = map(int, input().split())

def div(n):
    div_arr = []
    for i in range(1, n+1):
        if n % i == 0: div_arr.append(i)
    return div_arr

gcd = max([x for x in div(a) if x in div(b)])
lcm = int(a * b / gcd)

print(gcd, lcm, sep='\n')