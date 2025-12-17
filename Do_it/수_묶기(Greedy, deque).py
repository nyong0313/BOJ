# 1744
# 손으로 안풀고 바로 풀었더니 의식의 흐름대로임.
# 제대로 풀면 음수, 양수 나눠서 리스트 만들고, 1의 개수, 0의 개수 카운트해서 경우의 수 나눈 뒤, 계산해야함.
import sys, heapq
input = sys.stdin.readline
from collections import deque

n = int(input())
mylist = []

for _ in range(n):
    mylist.append(int(input()))
    # heapq.heappush(mylist, int(input()))

mylist.sort()
mylist = deque(mylist)
ans = 0
negative_number = True

while len(mylist):
    if len(mylist) == 1:
        # a = heapq.heappop(mylist)
        a = mylist.pop()
        ans += a
    
    elif negative_number:
        # a = heapq.heappop(mylist)
        # b = heapq.heappop(mylist)
        a = mylist.popleft()
        b = mylist.popleft()
        
        # 음수 값 처리.
        if b < 0:
            ans += a * b
        
        # 0 처리.
        elif a == 0:
            # heapq.heappush(mylist, b)
            mylist.appendleft(b)
            negative_number = False
        elif b == 0:
            ans += 0
            negative_number = False
        
        elif a < 0:
            ans += a
            mylist.appendleft(b)
            negative_number = False

        else:
            mylist.appendleft(b)
            mylist.appendleft(a)
            negative_number = False

    else:
        a = mylist.pop()
        b = mylist.pop()
        if a == 1 or b == 1:
            ans += a + b
        else:
            ans += a * b

print(ans)