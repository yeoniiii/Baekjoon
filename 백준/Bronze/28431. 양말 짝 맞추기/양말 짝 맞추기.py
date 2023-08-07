arr = [int(input())]
for _ in range(4):
    n = int(input())
    if n in arr:
        arr.remove(n)
    else: arr.append(n)
print(*arr)
    