import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

hear = set()
see = set()

for n in range(N):
    hear.add(input())
for m in range(M):
    see.add(input())

ans = sorted(list(hear & see))
    
print(len(ans))
print(*sorted(ans), sep='\n')