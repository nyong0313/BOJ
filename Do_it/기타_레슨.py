import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lesson = list(map(int, input().split()))

def bluelay_number(size):
    sum = 0
    count = 1
    for i in range(n):
        sum += lesson[i]
        if sum > size:
            count += 1
            sum = lesson[i]
    return count

def bin_search(start, end):
    global min_number
    while start <= end:
        mid = (start + end) // 2
        number = bluelay_number(mid)
        # 더 줄여서 검색.
        if number <= m:
            min_number = mid
            end = mid - 1

        # if number == m:
        #     min_number = mid
        #     end = mid - 1

        # elif number < m:
        #     min_number = mid
        #     end = mid - 1

        else:
            start = mid + 1

s = 0
e = 0
for i in lesson:
    if s < i:
        s = i
    e += i
min_number = e
bin_search(s, e)
print(min_number)