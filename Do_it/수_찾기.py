import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()

# def bin_search(k, start, end):
#     if start <= end:
#         mid = (end + start) // 2
#         if a[mid] == k:
#             return 1
#         elif k < a[mid]:
#             return bin_search(k, start, mid-1)
#         else:
#             return bin_search(k, mid+1, end)
        
#     else:
#         return 0

def bin_search(k, start, end):
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == k:
            return 1
        elif k < a[mid]:
            end = mid-1
        else:
            start = mid+1

    return 0
    
numbers = list(map(int, input().split()))
for i in range(m):
    print(bin_search(numbers[i], 0, n-1))
