from collections import Counter

S = input()
cnt = Counter(S)
arr = []

for i in range(ord('a'), ord('z')+1):
    c = chr(i)
    if c in cnt:
        arr.append(cnt[c])
    else:
        arr.append(0)
        
print(' '.join(map(str, arr)))