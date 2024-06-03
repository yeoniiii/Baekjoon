S = input()
N = len(S)

arr = []

for i in range(N):
    arr.append(S[i:])
    
print(*sorted(arr), sep='\n')