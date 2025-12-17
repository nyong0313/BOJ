# 1915
# dp[i][j] : i,j를 오른쪽 아래 꼭짓점으로 하는 가장 큰 정사각형 한변의 길이
# dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
# (i,j)가 1일때, 왼쪽, 오른쪽, 대각선 중 가장 작은 값에 1을 더한다. -> 직접 그려보면 이해가능
# 0일때는 사각형을 못만듦으로 무조건 0
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0 for _ in range(1000)]for _ in range(1000)]

maxNum = 0
for i in range(n):
    numbers = list((input()))
    for j in range(m):
        dp[i][j] = int(numbers[j])
        
        if dp[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            if maxNum < dp[i][j]:
                maxNum = dp[i][j]

print(maxNum*maxNum)