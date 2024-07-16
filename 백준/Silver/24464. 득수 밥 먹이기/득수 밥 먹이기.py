N = int(input())
past = [1, 2, 2]
if N >= 2:
    for i in range(2, N+1):
        now = [0, 0, 0]
        now[0] = (past[1] + past[2]) % 1000000007
        now[1] = (past[0]*2 + past[1] + past[2]) % 1000000007
        now[2] = (past[0]*2 + past[1]) % 1000000007
        past = now[:]
print(sum(past) % 1000000007)