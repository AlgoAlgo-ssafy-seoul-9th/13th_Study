def make_tree(node):
    if node == '.':
        return ''
    return node + make_tree(left[node]) + make_tree(right[node])


def mid(node):
    if node == '.':
        return ''
    return mid(left[node])+node+mid(right[node])

def post(node):
    if node == '.':
        return ''
    return post(left[node])+post(right[node])+node


n = int(input())
tree = []
left = {}
right = {}

for i in range(n):
    a, b, c = input().split()
    left[a] = b
    right[a] = c
# print(left)
# print(right)
print(make_tree('A'))
print(mid('A'))
print(post('A'))
