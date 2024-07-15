n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
idx = B.index(A[0])
B_fwd = B[idx:] + B[:idx]
B_back = B[idx+1:] + B[:idx+1]
B_back = B_back[::-1]
if A == B_fwd or A == B_back:
    print("good puzzle")
else:
    print("bad puzzle")