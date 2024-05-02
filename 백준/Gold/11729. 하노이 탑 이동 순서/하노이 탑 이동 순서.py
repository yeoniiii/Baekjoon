N = int(input())
num = [N, 0, 0]
arr = []

def hanoi(N, start, mid, end):
    if N == 1:
        arr.append([start, end])
        return

    hanoi(N-1, start, end, mid)
    arr.append([start, end])
    hanoi(N-1, mid, start, end)

hanoi(N, 1, 2, 3)
        
print(len(arr))
for i in range(len(arr)):
    print(arr[i][0], arr[i][1])