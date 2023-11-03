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

```

### [상미](./트리순회/상미.py)

```py

```

### [서희](./트리순회/서희.py)

```py

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

```

## [상미](./스티커/상미.py)

```py

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
