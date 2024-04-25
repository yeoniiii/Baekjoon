import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    
    n = int(input())
    cloth = {}
    for i in range(n):
        a, b = input().split()
        if b in cloth:
            cloth[b] += 1
        else:
            cloth[b] = 1
     
    ans = 1
    for key, value in cloth.items():
        ans *= (value + 1)
    print(ans -1)
        