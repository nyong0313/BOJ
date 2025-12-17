# 1328
# dp 배열 세우는 것부터 관건.
# dp[N][L][R] = N개의 빌딩, 왼쪽 L개, 오른쪽 R개 보일 수 있는 경우의 수.
n, l, r = map(int, input().split())
dp = [[[0 for _ in range(n+1)]for _ in range(n+1)]for _ in range(n+1)]
dp[1][1][1] = 1

for i in range(2, n+1):
    for j in range(n+1):
        for k in range(n+1):
            dp[i][j][k] = (dp[i-1][j-1][k] + dp[i-1][j][k-1] + dp[i-1][j][k]*(i-2)) % 1000000007

print(dp[n][l][r])