A = int(input())
B = int(input())
C = int(input())

n = A*B*C
t = [0]*10
n_list = list(map(int, str(n)))
for m in range(len(n_list)):
    for i in range(10):
        if n_list[m] == i:
            t[i] += 1
print(*t, sep='\n')