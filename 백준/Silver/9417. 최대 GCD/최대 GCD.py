import sys
input = lambda: sys.stdin.readline().rstrip()

def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a

N = int(input())
for n in range(N):
    arr = list(map(int, input().split()))
    ans = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                ans.append(gcd(arr[i], arr[j]))
    print(max(ans))