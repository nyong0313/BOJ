n = int(input())

# n일때, 미리 카운팅
count = 1
start_index = 1
end_index = 1
sum = 1

#start가 아니라 end_index, 다시 생각.
while start_index != n:

    if sum == n:
        count += 1
        #굳이 없어도 됨 어차피 else에서 걸러질테니까.
        # sum -= start_index
        # start_index += 1
        end_index += 1
        sum += end_index

    elif sum < n:
        end_index += 1
        sum += end_index

    else:
        sum -= start_index
        start_index += 1

print(count)