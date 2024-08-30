A, B = input().split()
if A == '0' or B == '0':
    print(0)
else:
    A = list(map(int, A))
    B = list(map(int, B))
    print(sum(A)*sum(B))