import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
colors = list(input().split())
m, k = map(int, input().split())

result = False
for i in range(m):
    plants = list(map(int, input().split()))
    isW = True
    for k in plants:
        if colors[k-1] == 'P':
            isW = False
            break
    if isW:
        result = True
        
if result:
    print('W')
else:
    print('P')