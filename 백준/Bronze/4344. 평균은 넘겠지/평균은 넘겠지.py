C = int(input())
for i in range(C):
    inp = input().split()
    N = int(inp[0])
    arr = list(map(int, inp[1:]))
    avg = sum(arr)/len(arr)
    ratio = sum([i>avg for i in arr])/len(arr)*100
    print(f'{ratio:.3f}%')
    