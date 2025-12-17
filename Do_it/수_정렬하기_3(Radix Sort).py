import sys
input = sys.stdin.readline

n = int(input())
# a = [0] * n
# maxLen = 0
# for i in range(n):
#     a[i] = int(input())

# # 최대 자릿수 계산
# maxLen = len(str(max(a)))

# for digit in range(maxLen):
#     # 큐 초기화
#     myqueue = [[] for _ in range(10)]

#     for i in a:
#         digit_value = (i // (10 ** digit)) % 10
#         myqueue[digit_value].append(i)

#     a = []
#     # 각 리스트의 모든 요소를 a에 추가
#     for i in myqueue:
#         a.extend(i)

# # 정렬된 리스트 출력
# for i in a:
#     print(i)

a = [0] * 10001
for i in range(n):
    a[int(input())] += 1

for i in range(10001):
    while a[i]:
        print(i)
        a[i] -= 1