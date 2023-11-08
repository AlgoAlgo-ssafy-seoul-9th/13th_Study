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

