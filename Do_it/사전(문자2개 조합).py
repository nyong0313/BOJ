# 1256
# 경우의 수 = (n+m)Cn  or  (n+m)Cm
# -> 전체 자리에서 한 문자가 들어갈 자리를 찾는 것과 같다. (문자가 2개 밖에 없으므로 나머지 자리에 다른 문자 들어간다.)
# 조합 점화식
n, m, k = map(int, input().split())
total = n+m
D = [[0 for _ in range(total+1)]for _ in range(total+1)]
for i in range(total+1):
    D[i][0] = 1
    D[i][i] = 1
    D[i][1] = i

for i in range(3, total+1):
    for j in range(2, total+1):
        D[i][j] = D[i-1][j] + D[i-1][j-1]

if D[total][n] < k:
    print(-1)
else:
    while n > 0 or m > 0:
        total = n+m
        if k <= D[total-1][n-1]:
            print("a", end="")
            n -= 1
        else:
            print("z", end="")
            k -= D[total-1][n-1]
            m -= 1