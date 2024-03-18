N = int(input())
for i in range(1, N+1):
    space = N-i
    print(' '*space + '*'*(2*i - 1))