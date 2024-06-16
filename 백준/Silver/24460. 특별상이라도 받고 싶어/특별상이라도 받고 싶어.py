import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
if N == 1:
    print(int(input()))
else:
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
   
    def find_chair(arr):
        l = len(arr)
        if l == 2:
            return sorted(arr[0]+arr[1])[1]
    
        a = find_chair([r[:l//2] for r in arr[:l//2]])
        b = find_chair([r[:l//2] for r in arr[l//2:]])
        c = find_chair([r[l//2:] for r in arr[:l//2]])
        d = find_chair([r[l//2:] for r in arr[l//2:]])
        return find_chair([[a, b], [c, d]])

    print(find_chair(arr))