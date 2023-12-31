# 13th_study

### 알고리즘 스터디 13주차

[백준 문제집](https://www.acmicpc.net/workbook/view/17259) <br/>

<!-- [프로그래머스](https://school.programmers.co.kr/learn/courses/30/lessons/148653) -->

# [트리순회]

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./트리순회/민웅.py)

```py
# 1991_트리순회_tree-traverse
import sys
input = sys.stdin.readline

def preorder(node):
    if node != '.':
        pre_lst.append(node)
        preorder(bt[node][0])
        preorder(bt[node][1])

def inorder(node):
    if node != '.':
        inorder(bt[node][0])
        in_lst.append(node)
        inorder(bt[node][1])

def postorder(node):
    if node != '.':
        postorder(bt[node][0])
        postorder(bt[node][1])
        post_lst.append(node)


N = int(input())

bt = {}
pre_lst = []
in_lst = []
post_lst = []
for _ in range(N):
    p, lc, rc = input().split()

    bt[p] = [lc, rc]
preorder('A')
inorder('A')
postorder('A')

print(''.join(pre_lst))
print(''.join(in_lst))
print(''.join(post_lst))
```

### [병국](./트리순회/병국.py)

```py
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

```

### [상미](./트리순회/상미.py)

```py
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

```

### [서희](./트리순회/서희.py)

```py
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

```

### [성구](./트리순회/성구.py)

```py
# 1991 트리 순회
import sys

input = sys.stdin.readline


def pre_order(N: int, tree: list, node: str) -> None:
    if node == ".":
        return
    print(node, end="")
    pre_order(N, tree, tree[node][0])
    pre_order(N, tree, tree[node][1])


def in_order(N: int, tree: list, node: str) -> None:
    if node == ".":
        return
    in_order(N, tree, tree[node][0])
    print(node, end="")
    in_order(N, tree, tree[node][1])


def post_order(N: int, tree: list, node: str) -> None:
    if node == ".":
        return
    post_order(N, tree, tree[node][0])
    post_order(N, tree, tree[node][1])
    if node != ".":
        print(node, end="")


def solution() -> None:
    N = int(input())
    tree = {}

    for _ in range(N):
        root, node1, node2 = input().strip().split()
        tree[root] = (node1, node2)
    pre_order(N, tree, "A")
    print()
    in_order(N, tree, "A")
    print()
    post_order(N, tree, "A")
    print()
    return


if __name__ == "__main__":
    solution()

```

</div>

</details>

<br><br>

# [스티커]

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./스티커/민웅.py)

```py
# 9465_스티커_sticker
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    sticker = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*(N+2) for _ in range(2)]
    # print(dp)
    for i in range(2, N+2):
        dp[0][i] = sticker[0][i-2] + max(dp[0][i-2], dp[1][i-2], dp[1][i-1])
        dp[1][i] = sticker[1][i-2] + max(dp[0][i-2], dp[1][i-2], dp[0][i-1])

    print(max(dp[0][-1], dp[1][-1]))
```

## [병국](./스티커/병국.py)

```py

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    for j in range(1,n):
        for i in range(2):
            if j == 1:
                if i == 0:
                    dp[i][j] = arr[i][j]+dp[i+1][j-1]
                else:
                    dp[i][j] = arr[i][j]+dp[i-1][j-1]
            else:
                if i == 0:
                    dp[i][j] = max(dp[i+1][j-1]+arr[i][j],arr[i][j]+dp[i+1][j-2])
                else:
                    dp[i][j] = max(dp[i-1][j-1]+arr[i][j],arr[i][j]+dp[i-1][j-2])
    print(max(dp[0][-1],dp[1][-1]))


```

## [상미](./스티커/상미.py)

```py
# 백준_ 9465 _스티커

T = int(input())

for t in range(T):
    n = int(input())
    sti = [[0] * n for _ in range(2)]
    for i in range(2):
        sti[i] = list(map(int, input().split()))
    # print(sti)



```

## [서희](./스티커/서희.py)

```py

```

## [성구](./스티커/성구.py)

```py
# 9465 sticker
import sys

input = sys.stdin.readline

def solution():
    for _ in range(int(input())):
        N = int(input())
        stickers = [0] * (N * 2)
        for i in range(2):
            arr = list(map(int, input().split()))
            for j in range(N):
                stickers[j * 2 + i] = arr[j]
        dp = [0] * (N * 2)
        dp[0] = stickers[0]
        dp[1] = stickers[1]
        for i in range(2, N * 2):
            # 홀수
            if i % 2:
                if 0 <= i - 3:
                    dp[i] = max(dp[i], dp[i - 3] + stickers[i])
                if 0 <= i - 4:
                    dp[i] = max(dp[i], dp[i - 4] + stickers[i])
                if 0 <= i - 5:
                    dp[i] = max(dp[i], dp[i - 5] + stickers[i])
            # 짝수
            else:
                if 0 <= i - 1:
                    dp[i] = max(dp[i], dp[i - 1] + stickers[i])
                if 0 <= i - 3:
                    dp[i] = max(dp[i], dp[i - 3] + stickers[i])
                if 0 <= i - 4:
                    dp[i] = max(dp[i], dp[i - 4] + stickers[i])
        print(max(dp[-1], dp[-2]))
    return


if __name__ == "__main__":
    solution()

```

</div>

</details>

<br><br>

# [양 구출 작전]

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./양%20구출%20작전/민웅.py)

```py


```

## [병국](./양%20구출%20작전/병국.py)

```py
import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline
def find_one(node,now):
    if node == 1:
        return now
    else:
        # 늑대가 아니라면 패스하고
        if animal[tree[node]] >= 0:
            return find_one(tree[node],now)
        # 늑대걸리면
        else:
            # 양 수 - 늑대 수 해주고,
            tmp = now + animal[tree[node]]

            # 양이 더 많으면 ?
            if tmp >= 0:
                # 늑대 없애준다
                animal[tree[node]] = 0
                return find_one(tree[node],tmp)

            # 늑대가 더 많으면 ?
            else:
                # 양 수 만큼 빼놓고 끝내자
                animal[tree[node]] += animal[node]
                return find_one(1,0)
    # print(animal)


def dfs(node):
    if animal[node] > 0:
        sheep = animal[node]
    else:
        sheep = 0
    for i in tree[node]:
        sheep += dfs(i)
    # 늑대면
    if animal[node] < 0:
        sheep = max(0,sheep+animal[node])
    return sheep


# 섬의 개수 n을 입력받음
n = int(input())
# w 인 경우 늑대
# s 인 경우 양
tree = [[] for _ in range(n+1)]
animal = [0 for _ in range(n+1)]

for i in range(2,n+1):
    t,a,p = input().split()
    a,p = int(a),int(p)
    if t == 'S':
        animal[i] = a
    else:
        animal[i] = -a
    tree[p].append(i)


answer = dfs(1)
print(answer)
```

## [상미](./양%20구출%20작전/상미.py)

```py

```

## [서희](./양%20구출%20작전/서희.py)

```py

```

## [성구](./양%20구출%20작전/성구.py)

```py

```

</div>

</details>

<br><br>

# [외판원순회]

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [민웅](./외판원순회/민웅.py)

```py


```

## [병국](./외판원순회/병국.py)

```py

```

## [상미](./외판원순회/상미.py)

```py

```

## [서희](./외판원순회/서희.py)

```py

```

## [성구](./외판원순회/성구.py)

```py

```

</div>

</details>
