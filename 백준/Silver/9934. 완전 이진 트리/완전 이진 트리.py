K = int(input())
inorder = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def sol(start, end, level):
    if start == end:
        tree[level].append(inorder[start])
        return
    center = (start + end) // 2
    tree[level].append(inorder[center])
    sol(start, center-1, level+1)
    sol(center+1, end, level+1)

sol(0, len(inorder)-1, 0)
for a in tree:
    print(*a)