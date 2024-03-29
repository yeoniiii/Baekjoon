import sys
input = lambda: sys.stdin.readline().rstrip()
#sys.recursionlimit(10**6)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        if a != b:
            union_parent(parent, a, b)
    elif c == 1:
        if a == b:
            print("YES")
        elif find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")