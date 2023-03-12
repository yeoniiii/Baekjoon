N = int(input())

r = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in r:
    if i==v :
        cnt += 1
print(cnt)