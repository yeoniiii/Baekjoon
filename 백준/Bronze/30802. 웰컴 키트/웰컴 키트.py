N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

T_num = 0
for s in size:
    if s % T == 0:
        T_num += s//T
    else:
        T_num += s//T + 1
    
print(T_num)
print(N//P, N%P)