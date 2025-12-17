n = int(input())
value = [0] * n
for i in range(n):
    value[i] = int(input())

num_value = 0
mystack = []
count = 0
result = []

for i in range(1, n+1):
    result.append("+")
    count += 1
    mystack.append(i)
    
    # mystack 조건 ** 안넣으면 mystack[-1]에서 out of range 발생
    if mystack and value[num_value] < mystack[-1]:
        print("NO")
        exit()

    # mystack 조건 ** 안넣으면 mystack[-1]에서 out of range 발생
    while mystack and value[num_value] == mystack[-1]:
        result.append("-")
        count += 1
        mystack.pop()
        num_value += 1

    # mystack 조건 ** 안넣으면 mystack[-1]에서 out of range 발생
    if mystack and value[num_value] < mystack[-1]:
        print("NO")
        exit()

    # mystack 조건 ** 안넣으면 mystack[-1]에서 out of range 발생
    while mystack and value[num_value] == mystack[-1]:
        result.append("-")
        count += 1
        mystack.pop()
        num_value += 1

for i in range(count):
    print(result[i])