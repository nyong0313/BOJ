# 9252
# LCS : 부분수열이기 때문에 문자 사이를 건너뛰어 공통되면서 가장 긴 부분 문자열을 찾음.
import sys
sys.setrecursionlimit(1000000)
a = list(input())
b = list(input())
dp = [[0 for _ in range(1001)]for _ in range(1001)]
ans = []

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(a)][len(b)])

def getText(r, c):
    if r == 0 or c == 0:
        return
    if a[r-1] == b[c-1]:
        ans.append(a[r-1])
        getText(r-1, c-1)
    else:
        if dp[r-1][c] > dp[r][c-1]:
            getText(r-1, c)
        else:
            getText(r, c-1)

getText(len(a), len(b))

for i in range(len(ans)-1, -1, -1):
    print(ans[i], end="")