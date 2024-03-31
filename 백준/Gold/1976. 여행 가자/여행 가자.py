import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

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

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if i != j and arr[j] == 1:
            union_parent(parent, i+1, j+1)
          
plan = list(map(int, input().split()))

plan_parent = set()
for p in plan:
    plan_parent.add(parent[p])

if len(plan_parent) == 1:
    print("YES")
else:
    print("NO")