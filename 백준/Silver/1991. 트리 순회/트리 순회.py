N = int(input())
tree = {}

for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def preorder(root):
    if root != '.':
        print(root, end = '')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end = '')
        inorder(tree[root][1])
    
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = '')

preorder('A')
print() # 띄어쓰기 용도
inorder('A')
print() # 띄어쓰기 용도
postorder('A')