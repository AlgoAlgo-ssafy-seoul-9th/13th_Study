# 백준_ 1991_ 트리순회

def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right

def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root             # 줄 바꿈 안되도록 end = ''
        inorder(tree[root][1])  # right

def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # roo

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = list(map(str, input().split()))
    tree[root] = left, right

preorder('A')
print()
inorder('A')
print()
postorder('A')
