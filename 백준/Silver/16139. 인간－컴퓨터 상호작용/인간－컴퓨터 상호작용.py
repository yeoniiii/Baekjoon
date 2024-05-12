import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
q = int(input())

cumnum = {}
for n in range(ord('a'), ord('z')+1):
    a = chr(n)
    cumnum[a] = [0]
    for i in range(len(s)):
        if s[i] == a:
            cumnum[a].append(cumnum[a][i] + 1)
        else:
            cumnum[a].append(cumnum[a][i])

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    print(cumnum[a][r+1] - cumnum[a][l])