N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def find_sum(idx, s):
    global cnt
    
    if idx >= N:
        return
    
    s += arr[idx]
    if s == S:
        cnt += 1
        
    find_sum(idx+1, s)
    find_sum(idx+1, s-arr[idx])

find_sum(0, 0)
print(cnt)