N = int(input())
A = list(map(int, input().split()))

change = []
for i in range(N):
    if A[i] == i+1:
        continue
        
    j = A.index(i+1)
    change.append([i+1, j+1])
    A[i:j+1] = A[i:j+1][::-1]
    
print(len(change))
for c in change:
    print(*c)