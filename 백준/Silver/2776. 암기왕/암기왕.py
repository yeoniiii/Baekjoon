import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    N = int(input())
    note1 = set(list(map(int, input().split())))
    M = int(input())
    note2 = list(map(int, input().split()))
    for n in note2:
        if n in note1:
            print(1)
        else:
            print(0)