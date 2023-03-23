T = int(input())
for i in range(T):
    R, S = input().split()
    S = [s*int(R) for s in S]
    print(''.join(S))
        