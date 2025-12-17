import sys
input = sys.stdin.readline
n = int(input())
mylist = []
for i in range(n):
    x = int(input())
    mylist.append(x)

for i in range(n):
    for j in range(i, n):
        if mylist[i] > mylist[j]:
            buffer = mylist[i]
            mylist[i] = mylist[j]
            mylist[j] = buffer

for i in range(n):
    print(mylist[i])