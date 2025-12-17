# 1463
n = int(input())
D = [0]*(n+1)

for i in range(2, n+1):
    D[i] = D[i-1] + 1 #1 빼는 방법
    if i % 3 == 0:
        D[i] = min(D[i], D[i//3] + 1)
    elif i % 2 == 0:
        D[i] = min(D[i], D[i//2] + 1)

print(D[n])



# ans = []
# if n % 3 == 0:
#     temp = n
#     cnt = 0
#     while temp % 3 == 0:
#         temp = temp // 3
#         cnt += 1
#     while temp % 2 == 0:
#         temp = temp // 2
#         cnt += 1
#     if temp == 1:
#         ans.append(cnt)

# if n % 2 == 0:
#     temp = n
#     cnt = 0
#     while temp % 2 == 0:
#         temp = temp // 2
#         cnt += 1
#     if temp == 1:
#         ans.append(cnt)

# temp = n
# cnt = 0
# while temp % 3 != 0:
#     if temp == 1:
#         break
#     temp -= 1
#     cnt += 1
# while temp % 3 == 0:
#     temp = temp // 3
#     cnt += 1
# while temp % 2 == 0:
#     temp = temp // 2
#     cnt += 1
# if temp == 1:
#     ans.append(cnt)

# print(min(ans))