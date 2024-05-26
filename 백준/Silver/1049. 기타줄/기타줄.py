import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
min_pack, min_one = 1001, 1001
for i in range(M):
    pack, one = map(int, input().split())
    min_pack = min(pack, min_pack)
    min_one = min(one, min_one)

min_pack = min(min_pack, min_one*6)

print(min((N//6 + 1) * min_pack, (N//6) * min_pack + (N%6) * min_one))