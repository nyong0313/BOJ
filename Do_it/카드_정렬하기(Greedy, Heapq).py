import sys
import heapq
# from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
mylist = []
# myqueue = PriorityQueue()
for _ in range(n):
    heapq.heappush(mylist, int(input()))

ans = 0
while len(mylist) > 1:
    a = heapq.heappop(mylist)
    b = heapq.heappop(mylist)
    ans += a + b
    heapq.heappush(mylist, a+b)

print(ans)