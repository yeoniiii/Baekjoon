import sys
input = sys.stdin.readline

T = int(input())
apart = [[i+1 for i in range(15)]]
for j in range(1000):
    apart.append([sum(apart[j][0:(i+1)]) for i in range(15)])

for t in range(T):
    k = int(input())
    n = int(input())
    print(apart[k][n-1])