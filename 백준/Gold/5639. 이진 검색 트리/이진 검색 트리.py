import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

preorder = [] # root > left > right

while True:
    inp = input()
    if inp == '':
        break
    preorder.append(int(inp))
    
N = len(preorder)

postorder = [] # left > right > root
def find_postorder(l, r):
    if l > r:
        return
    
    root = preorder[l]
    postorder.append(root)
    
    idx = l
    while idx <= r:
        if preorder[idx] <= root:
            idx += 1
        else:
            break
    
    find_postorder(idx, r)
    find_postorder(l+1, idx-1)
    
find_postorder(0, N-1)
print(*postorder[::-1], sep='\n')