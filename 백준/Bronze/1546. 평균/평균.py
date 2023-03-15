N = int(input())

arr = list(map(int, input().split()))
S = sum(arr)
M = max(arr)

print(S/N/M*100)