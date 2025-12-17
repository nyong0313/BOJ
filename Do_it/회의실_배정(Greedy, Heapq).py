import sys, heapq
input = sys.stdin.readline

n = int(input())
mylist = []
for i in range(n):
    i, j = map(int, input().split())
    # 정렬 기준 때문에 튜플의 순서를 바꿈.
    heapq.heappush(mylist, (j, i))

count = 0
finish_time = 0
for i in range(n):
    # a[0] = finish_time(j), a[1] = start_time(i)
    a = heapq.heappop(mylist)
    if a[1] >= finish_time:
        finish_time = a[0]
        count += 1

print(count)