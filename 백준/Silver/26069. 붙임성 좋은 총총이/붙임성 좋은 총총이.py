import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dance = {'ChongChong':1}
for i in range(N):
    meet = list(input().split())
    for m in range(2):
        if meet[m] in dance:
            dance[meet[1-m]] = 1
            
print(len(dance))