import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())

inorder = list(map(int, input().split())) # left > root > right
postorder = list(map(int, input().split())) # left > right > root

inorder_idx = [0] * (n+1)
for idx, i in enumerate(inorder):
    inorder_idx[i] = idx

def preorder(inorder_l, inorder_r, postorder_l, postorder_r):
    if postorder_l > postorder_r:
        return
    
    root = postorder[postorder_r]
    print(root, end=' ')
    
    root_idx = inorder_idx[root]
    len_l = root_idx - inorder_l
    len_r = inorder_r - root_idx
    
    preorder(inorder_l, root_idx-1, postorder_l, postorder_l+len_l-1)
    preorder(root_idx+1, inorder_r, postorder_r-len_r, postorder_r-1)
    
preorder(0, n-1, 0, n-1)