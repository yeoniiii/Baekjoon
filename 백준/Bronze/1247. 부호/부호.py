import sys
input = sys.stdin.readline

l = [None]*3

for i in range(3):
    N = int(input())
    sum = 0
    
    for n in range(N):
        sum += int(input())

    if sum == 0: l[i] = "0"
    elif sum > 0: l[i] = "+"
    else: l[i] = "-"
print(*l, sep='\n')