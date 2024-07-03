import math

N = int(input())
if N <= 2:
    print(N-1)
else:
    a = int(math.log2(N-1))
    print(2**a + 2**(a-1) + (N-1-2**a)//2)