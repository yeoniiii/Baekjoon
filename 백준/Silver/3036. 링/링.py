from fractions import Fraction

N = int(input())
ring = list(map(int, input().split()))

for i in range(1, N):
    ans = Fraction.from_float(ring[0] / ring[i]).limit_denominator(100000) 
    if ans % 1 == 0:
        ans = str(ans)+'/'+'1'
    print(ans)