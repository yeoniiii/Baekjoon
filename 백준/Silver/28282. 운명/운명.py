X, K = map(int, input().split())
A = list(map(int, input().split()))
left_col, right_col = {}, {}
for i in range(2*X):
    if i < X:
        if A[i] in left_col:
            left_col[A[i]] += 1
        else:
            left_col[A[i]] = 1
    else:
        if A[i] in right_col:
            right_col[A[i]] += 1
        else:
            right_col[A[i]] = 1
        
ans = 0
for i in left_col.keys():
    for j in right_col.keys():
        if i != j:
            ans += left_col[i] * right_col[j]
print(ans)