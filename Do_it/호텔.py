# [백준 12865번 평범한 배낭] [백준 2758번 로또]  [백준 1106번 호텔]
import sys
input = sys.stdin.readline
c, n = map(int, input().split())
cost_list = [list(map(int,input().split())) for _ in range(n)]

dp = [sys.maxsize]*(c+100) # C명보다 많은 고객 수에서 최소비용 가능!! (+ 최대 100원)
dp[0]=0

for cost, num_people in cost_list:
    for i in range(num_people,c+100):
        dp[i] = min(dp[i-num_people]+cost, dp[i])
 
print(min(dp[c:])) #인덱스 c부터 끝까지



# myList = []
# initList = []
# max_b = (0, 0)
# for i in range(n):
#     a, b = map(int, input().split())
        
#     if max_b[1] < b:
#         max_b = (a, b)
#     myList.append((a, b))

#     w = a
#     p = b
#     temp = [0]*(c+1)
#     for j in range(1, c+1):
#         if j > p:
#             w += a
#             p += b
#         temp[j] = w
#     initList.append(temp)


# dp = [sys.maxsize]*(c+1)
# dp[0]=0

# for i in range(1, max_b[1]+1):
#     for j in range(n):
#         if initList[j][i] < dp[i]:
#             dp[i] = initList[j][i]

# for i in range(max_b[1], c+1):
#     for j in range(n):
#         if dp[i-myList[j][1]] + dp[myList[j][1]] < dp[i]:
#             dp[i] = dp[i-myList[j][1]] + dp[myList[j][1]]

# print(dp[c])