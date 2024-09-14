import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import permutations

arr = list(permutations(list(range(1, 10)), 3))

N = int(input())
for n in range(N):
    quest, s, b = map(int, input().split())
    tmp = []
    
    for a in arr:
        cnt_s, cnt_b = 0, 0
        
        for i, q in enumerate(str(quest)):
            if int(q) == a[i]:
                cnt_s += 1
            elif int(q) in a:
                cnt_b += 1
        
        if cnt_s == s and cnt_b == b:
            tmp.append(a)
    arr = tmp
    
print(len(arr))