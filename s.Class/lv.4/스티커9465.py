import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    myList = [[0 for _ in range(n)]for __ in range(2)]
    for i in range(2):
        myList[i] = list(map(int, input().split()))

    dp = [[0 for _ in range(2)]for __ in range(n)]

    dp[0][0] = myList[0][0]
    dp[0][1] = myList[1][0]
    if n == 1:
        print(max(dp[0]))
        continue
    
    dp[1][0] = dp[0][1] + myList[0][1]
    dp[1][1] = dp[0][0] + myList[1][1]
    if n == 2:
        print(max(dp[1]))
        continue

    for i in range(2, n):
        dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + myList[0][i]
        dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + myList[1][i]

    print(max(dp[n-1]))



# for _ in range(t):
#     n = int(input())
#     myList = [[0 for _ in range(n)]for __ in range(2)]
#     for i in range(2):
#         myList[i] = list(map(int, input().split()))

#     dp = [()]*n
#     if myList[0][0] > myList[1][0]:
#         dp[0] = (myList[0][0], 0)
#     else:
#         dp[0] = (myList[1][0], 1)

#     for i in range(1, n):
#         dp[i] = (dp[i-1][0] + myList[(dp[i-1][1] + 1) % 2][i], dp[i-1][1] + 1)

#         if i > 1:
#             temp = dp[i-2][0] + myList[(dp[i-2][1] + 1) % 2][i]
#             if temp > dp[i][0]:
#                 dp[i-1] = dp[i-2]
#                 dp[i] = (temp, dp[i-2][1] + 1)
#         else:
#             temp = myList[dp[i-1][1]][i]
#             if temp > dp[i][0]:
#                 dp[i-1] = (myList[(dp[i-1][1] + 1) % 2][i-1], (dp[i-1][1] + 1) % 2)
#                 dp[i] = (temp + dp[i-1][0], (dp[i-1][1] + 1) % 2)
        
#     print(dp[n-1][0])