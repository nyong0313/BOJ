# 2342
# dp[N][L][R] : N개 수행하고 왼발, 오른발 해당 위치일때 값.
# 오른발 움직이는 경우, 왼발 움직이는 경우로 나눠, 모든 경우의 수를 계산함.
import sys
inputList = list(map(int, input().split()))

dp = [[[sys.maxsize for _ in range(5)]for __ in range(5)]for ___ in range(100001)]

# i->j 이동할때 비용 값 미리 저장
mp = [[0, 2, 2, 2, 2],
      [2, 1, 3, 4, 3],
      [2, 3, 1, 3, 4],
      [2, 4, 3, 1, 3],
      [2, 3, 4, 3, 1]]

dp[0][0][0] = 0
s = 1
index = 0

while inputList[index] != 0:
    n = inputList[index]

    for i in range(5):
        if i == n:
            continue
        for j in range(5):
            dp[s][i][n] = min(dp[s][i][n], dp[s-1][i][j] + mp[j][n])

    for j in range(5):
        if j == n:
            continue
        for i in range(5):
            dp[s][n][j] = min(dp[s][n][j], dp[s-1][i][j] + mp[i][n])

    s += 1
    index +=1

s -= 1
result = dp[s][0][0]
for i in range(5):
    for j in range(5):
        result = min(result, dp[s][i][j])

print(result)


# a = list(map(int, input().split()))
# step = [0] * 2
# sum = 0

# for i in a:
#     if i == 0:
#         break
#     if step[0] == 0:
#         step[0] = i
#         sum += 2
#     elif step[1] == 0:
#         step[1] = i
#         sum += 2
#     elif step[0] == i or step[1] == i:
#         sum += 1
#     elif (step[0] + 1) % 4 == i or (step[0] - 1) % 4 == i:
#         step[0] = i
#         sum += 3
#     elif (step[1] + 1) % 4 == i or (step[1] - 1) % 4 == i:
#         step[1] = i
#         sum += 3
#     elif i == 4:
#         if (step[0] + 1) % 4 == 0 or (step[0] - 1) % 4 == 0:
#             step[0] = i
#             sum += 3
#         elif (step[1] + 1) % 4 == 0 or (step[1] - 1) % 4 == 0:
#             step[1] = i
#             sum += 3
#         else:
#             step[0] = i
#             sum += 4
#     else:
#         step[0] = i
#         sum += 4

# print(sum)