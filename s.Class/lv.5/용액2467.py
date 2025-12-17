import sys
input = sys.stdin.readline
n = int(input())
myList = list(map(int, input().split()))
a = 0
b = n-1
result = sys.maxsize

while a < b:
    if result >= abs(myList[a] + myList[b]):
        result = abs(myList[a] + myList[b])
        minA = a
        minB = b
    if abs(myList[a]) < abs(myList[b]):
        b -= 1
    elif abs(myList[a]) > abs(myList[b]):
        a += 1
    else:
        break

print(myList[minA], myList[minB])