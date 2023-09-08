import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
arr = []
for n in range(N):
    arr.append(int(input()))
    
mean = round(sum(arr)/N)
med = sorted(arr)[N//2]
count = Counter(arr)
modes = []
for el, cnt in count.items():
    if cnt == max(count.values()):
        modes.append(el)
if len(modes) > 1:
    modes.remove(min(modes))
mod = min(modes)
rang = max(arr) - min(arr)
print(mean, med, mod, rang, sep='\n')