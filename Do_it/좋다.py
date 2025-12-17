n = int(input())
A = list(map(int, input().split()))

count = 0
A.sort()

for k in range(n):
    i=0
    j=n-1

    while i<j:
        sum = A[i] + A[j]

        if sum == A[k]:
            if i == k:
                i += 1

            elif j == k:
                j -= 1

            else:
                count += 1
                break

        elif sum > A[k]:
            j -= 1

        else:
            i += 1

print(count)


# # 7번 문제과 같은 로직 !! but, 틀림. 문제를 잘못 이해함. 근데 예시가 좀 불친절하긴해. 
# 반례 : 0 0 0 1 1 2 답: 6
# for k in range(2, n):

#     i = 0
#     j = k - 1

#     while i < j:
#         sum = A[i] + A[j]

#         if sum == A[k]:
#             count += 1
#             break

#         elif sum < A[k]:
#             i += 1

#         else:
#             j -= 1

# print(count)


#풀긴했는데 clean하지 않음. + 시간 초과
# for k in range(n):

#     for i in range(k-1):
#         for j in range(i+1, k):
#             sum = A[i] + A[j]
#             if sum == A[k]:
#                 count += 1
#         if sum == A[k]:
#             break

#교재
# for k in range(n):
#     i = 0
#     j = n -1 
#     while i < j:
#         if A[i] + A[j] == A[k]:
#             if i != k and j != k:
#                 count += 1
#                 break

#             elif i == k:
#                 i += 1
            
#             elif j == k:
#                 j -= 1

#         elif A[i] + A[j] < A[k]:
#             i += 1

#         else:
#             j -= 1
# print(count)