import sys
input = lambda: sys.stdin.readline().rstrip()
arr = [0]*26
ans = ''

for i in range(int(input())):
    name = input()
    n = ord(name[0]) - ord('a')
    arr[n] += 1
for a in range(len(arr)):
    if arr[a] >= 5:
        ans += chr(a+ord('a'))
if ans == '': print('PREDAJA')
else: print(ans)