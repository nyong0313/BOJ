import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
S = [0] * (n+1)

for i in range(1, n+1):
    S[i] = S[i-1] + A[i]

remainder = [0] * m
count = 0
for i in range(1, n+1):
    S[i] = (S[i]) % m
    if S[i] == 0:
        count += 1
    
    remainder[S[i]] += 1
    
for i in range(m):
    if remainder[i] > 1:
        # /연산하면 float 변수 나오므로 //연산 ***
        count += (remainder[i] * (remainder[i] - 1)) // 2

print(count)


# 시간초과 떴음. ***
# for i in range(1, n+1):
#     for j in range(i, n+1):
#         if((S[j] - S[i-1]) % m == 0):
#             count += 1