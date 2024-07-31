N = int(input())
arr = [1, 1]
for i in range(2, 21):
    arr.append(arr[-1]*i)
sum = 0
yes = 0
for i in range(20, -1, -1):
    if sum + arr[i] < N:
        sum += arr[i]
    elif sum + arr[i] == N:
        yes = 1
        break
if yes == 0:
    print("NO")
else:
    print("YES")