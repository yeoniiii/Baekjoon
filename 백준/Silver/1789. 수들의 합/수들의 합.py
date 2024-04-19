N = int(input())
cnt = 0
for i in range(1, 4294967295):
    N -= i
    if N < 0:
        break
    cnt += 1
print(cnt)