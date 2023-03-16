S = input()

arr = [-1 for i in range(26)]
for i in S:
    arr[ord(i) - 97] = S.index(i)
print(' '.join(list(map(str, arr))))