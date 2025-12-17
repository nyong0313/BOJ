# 1300
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = k
while start <= end:
    mid = (end + start) // 2
    cnt = 0
    for i in range(1, n+1):
        cnt += min((mid // i), n)
    
    if cnt < k:
        start = mid + 1
    else:
        ans = mid
        end = mid -1

print(ans)




# 메모리 초과
# a = [[]for _ in range(n)]
# b = []
# for i in range(n):
#     for j in range(n):
#         # a[i].append((i+1)*(j+1))
#         b.append((i+1)*(j+1))

# b.sort()

# print(b[k-1])