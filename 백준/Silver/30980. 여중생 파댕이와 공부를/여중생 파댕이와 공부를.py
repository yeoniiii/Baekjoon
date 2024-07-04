import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ans = [''] * 3*N
for i in range(N):
    space1 = input()
    arr = list(input().split('.'))
    for q in arr:
        if q:
            a, c = q.split('=')
            a, b = a.split('+')
            if len(c) == 2:
                sep = 1
            else:
                sep = 2
            if int(a) + int(b) == int(c):
                ans[3*i] += '.'+'*'*len(q)+'.'*sep
                ans[3*i+1] += '*'+q+'*'+'.'*(sep-1)
                ans[3*i+2] += '.'+'*'*len(q)+'.'*sep
            else:
                new_q = a+'/'+b+'='+c
                ans[3*i] += '.'*3+'/'+'.'*4
                ans[3*i+1] += '.'+new_q+'.'*sep
                ans[3*i+2] += '.'*1+'/'+'.'*6
    space2 = input()
print(*ans, sep='\n')