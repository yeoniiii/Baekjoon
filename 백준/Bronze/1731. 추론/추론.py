N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
if arr[1]**2 == arr[0] * arr[2]:
    print(arr[-1] * (arr[1]//arr[0]))
else:
    print(arr[-1] + (arr[1]-arr[0]))