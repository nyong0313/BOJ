# 13251
# 각 mCk 더하고 나누기 nCk
m = int(input())
c = list(map(int, input().split()))
k = int(input())

n = sum(c)
D = [[0 for _ in range(n+1)]for _ in range(n+1)]

for i in range(n+1):
    D[i][0] = 1
    D[i][1] = i
    D[i][i] = 1

for i in range(3, n+1):
    for j in range(2, n+1):
        D[i][j] = D[i-1][j] + D[i-1][j-1]

ans = 0
for t in range(m):
    ans += D[c[t]][k]

ans = ans / D[n][k]
print(ans)