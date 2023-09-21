N = int(input())
arr = list(map(int, input().split()))
y = m = 0

for n in arr:
    y += (n // 30 + 1) * 10
    m += (n // 60 + 1) * 15

if y == m:
    print('Y M', y)
elif y < m:
    print('Y', y)
elif m < y:
    print('M', m)