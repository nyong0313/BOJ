# 11049
# 부분의 문제가 해결됐다고 가정하고 점화식 떠올리기
import sys
# sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
arr = [0]*n
dp = [[sys.maxsize for _ in range(n)]for __ in range(n)]

for i in range(n):
    r, c = map(int, input().split())
    arr[i] = (r, c)

# 연산
def execute(s, e):
    if dp[s][e] != sys.maxsize:
        return dp[s][e]
    if s == e:
        return 0
    elif e-s == 1:
        return arr[s][0]*arr[s][1]*arr[e][1]
    else:
        result = sys.maxsize
        for i in range(s, e):
            result = min(result, execute(s, i) + execute(i+1, e) + arr[s][0]*arr[i][1]*arr[e][1])
            dp[s][e] = result
        return dp[s][e]

execute(0, n-1)
    
print(dp[0][n-1])