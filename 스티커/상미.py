# 백준_ 9465 _스티커

T = int(input())

for t in range(T):
    n = int(input())
    sti = [[0] * n for _ in range(2)] 
    for i in range(2):
        sti[i] = list(map(int, input().split()))
    # print(sti)
    

