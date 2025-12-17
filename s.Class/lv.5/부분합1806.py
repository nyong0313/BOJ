# 연속된 수열 -> 투포인터 고려하기
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
myList = list(map(int, input().split()))

a, b = 0, 0
absum = myList[0]
cnt = sys.maxsize

while True:
    if absum >= s:
        if cnt > b-a:
            cnt = b-a+1
        absum -= myList[a]
        a += 1
    else:
        b += 1
        if b == n: 
            break
        absum += myList[b]

print(cnt if cnt != sys.maxsize else 0)