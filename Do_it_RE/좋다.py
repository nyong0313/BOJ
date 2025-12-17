# ch3 - 8/1253
# 투포인터
# 리스트 정렬한다음 찾는 숫자보다 작은 것들만 고려했는데 그럼 안되고 매번 처음부터 끝까지 찾아야함.
import sys
input = sys.stdin.readline
n = int(input())

a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(n):
    start = 0
    end = n-1
    while start < end:
        if start == i:
            start += 1
        elif end == i:
            end -= 1
        else:
            sumA = a[start] + a[end]
            if sumA == a[i]:
                ans += 1
                break
            elif sumA < a[i]:
                start += 1
            else:
                end -= 1

print(ans)




# import sys
# input = sys.stdin.readline
# n = int(input())

# a = list(map(int, input().split()))
# a.sort()

# def find(i):
#     start = 0
#     end = i-1
#     while start < end:
#         sumA = a[start] + a[end]
#         if sumA == a[i]:
#             return True
#         elif sumA < a[i]:
#             start += 1
#         else:
#             end -= 1
#     return False

# ans = 0
# if n >= 3:
#     if a[0] == a[1] + a[2]:
#         ans += 1
#     if a[1] == a[0] + a[2]:
#         ans += 1
#     if a[2] == a[0] + a[1]:
#         ans += 1

# for i in range(3, n):
#     if find(i):
#         ans += 1

# print(ans)