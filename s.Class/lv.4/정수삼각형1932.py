import sys
input = sys.stdin.readline
n = int(input())
t = [[0 for _ in range(n)]for __ in range(n)]

for i in range(n):
    t[i] = list(map(int, input().split()))
    
dp = [[0 for _ in range(n)]for __ in range(n)]
dp[0][0] = t[0][0]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + t[i][0]

    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + t[i][j]

    dp[i][i] = dp[i-1][i-1] + t[i][i]

print(max(dp[n-1]))