import sys
input = lambda: sys.stdin.readline().rstrip()
import math

C = int(input())
for c in range(C):
    S, N, T, L = input().split(' ')
    limit = 10 ** 8 * int(L)
    N, T = int(N), int(T)
    if (S == 'O(N)' and N * T <= limit) or \
    (S == 'O(N^2)' and N**2*T <= limit) or \
    (S == 'O(N^3)' and N**3*T <= limit) or \
    (S == 'O(2^N)' and 2**N*T <= limit) or \
    (S == 'O(N!)' and math.factorial(N)*T <= limit):
        print("May Pass.")
    else:
        print("TLE!")