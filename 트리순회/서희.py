import sys

N = int(input())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='') # root
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='') # root
        inorder(tree[root][1])
        
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='') # root
        

preorder("A")    
print()
inorder("A")    
print()
postorder("A")    