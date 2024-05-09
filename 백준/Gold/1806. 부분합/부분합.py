N, S = map(int, input().split())
A = list(map(int, input().split()))

if S > sum(A):
    print(0)
else:
    min_l = N+1

    start, end = 0, 1
    s = A[start]

    while True:
        if s < S:
            if end < N:
                s += A[end]
                end += 1
            else:
                break
        else:
            l = end - start
            min_l = min(min_l, l)
            s -= A[start]
            start += 1
    
    print(min_l)