N = int(input())
sum = 0
arr = []
for i in str(N):
    sum += int(i)
    arr.append(int(i))
if '0' in str(N) and sum % 3 == 0:
    arr.sort(reverse=True)
    print(''.join(map(str, arr)))
else:
    print(-1)