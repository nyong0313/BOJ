# 2775
D = [[0 for _ in range(15)]for _ in range(15)]
for b in range(15):
    D[0][b] = b
for a in range(1, 15):
    for b in range(1, 15):
        D[a][b] = D[a-1][b] + D[a][b-1]

testCase = int(input())
for _ in range(testCase):
    k = int(input())
    n = int(input())
    print(D[k][n])