import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
cnt = 0
for i in range(N):
    inp = input()
    if inp == 'ENTER':
        name = {}
    elif inp not in name:
        cnt += 1
        name[inp] = 1
print(cnt)