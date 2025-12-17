# 1010
# mCn
testCase = int(input())
for _ in range(testCase):
    n, m = map(int, input().split())
    D = [[0 for _ in range(m+1)]for _ in range(m+1)]

    for i in range(m+1):
        D[i][0] = 1
        D[i][1] = i
        D[i][i] = 1

    for i in range(3, m+1):
        for j in range(2, i):
            D[i][j] = D[i-1][j] + D[i-1][j-1]

    print(D[m][n])