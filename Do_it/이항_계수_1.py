# 11050
# 이항계수 = 조합 nCk
n, k = map(int, input().split())
ans = 1

for i in range(k):
    ans *= n - i

for i in range(k, 1, -1):
    ans = ans // i

print(ans)