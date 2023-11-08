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