import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
J = int(input())
    
def move(n):
    global start, end
    i = 0
    while True:
        if (1 > start+i or end+i >= N+1) and (1 > start-i or end-i >= N+1):
            break
        if 1<=start+i and end+i<N+1:
            if start+i <= n <= end+i:
                start += i
                end += i
                return i
        if 1<=start-i and end-i<N+1:
            if start-i <= n <= end-i:
                start -= i
                end -= i
                return i
        i += 1
            
num = 0
start, end = 1, M
for j in range(J):
    num += move(int(input()))
print(num)