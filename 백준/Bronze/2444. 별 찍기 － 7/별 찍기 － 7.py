N=int(input())
for i in range(1,2*N):
    if i <= N:
        space = N-i
        star = 2*i-1
    else :
        space = i-N
        star = 2*(2*N-i)-1
    print(' '*space+'*'*star)