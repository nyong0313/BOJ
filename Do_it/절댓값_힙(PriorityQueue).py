# 자료구조 PriorityQueue를 알고 있느냐.
from queue import PriorityQueue
import sys
input = sys.stdin.readline # *** 없으면 시간초과

n = int(input())
myque = PriorityQueue()

for i in range(n):
    x = int(input())
    if x == 0:
        if myque.empty():
            print(0)
        else:
            print(myque.get()[1])

    else:
        myque.put((abs(x), x))