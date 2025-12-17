# 자바에서는 substring()과 배열 저장하는 내장함수 쓰면 바로 풀림.
import sys
input = sys.stdin.readline
str_value = input()
value = int(str_value)
mylist = []

for i in range(len(str_value)-1):
    mylist.append(value%10)
    value = int(value/10)

for i in range(len(str_value)-1):
    max = mylist[i]
    max_index = i
    for j in range(i+1, len(str_value)-1):
        if max < mylist[j]:
            max = mylist[j]
            max_index = j

    if max_index != i:
        mylist[max_index] = mylist[i]
        mylist[i] = max


for i in range(len(str_value)-1):
    print(mylist[i], end="")