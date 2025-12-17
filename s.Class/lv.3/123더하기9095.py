myList = [0]*11
myList[1]=1
myList[2]=2
myList[3]=4
for i in range(4, 11):
    myList[i] = myList[i-1] + myList[i-2] + myList[i-3]

t = int(input())
for i in range(t):
    n = int(input())
    print(myList[n])