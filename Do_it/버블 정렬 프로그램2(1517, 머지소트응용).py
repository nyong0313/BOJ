def mergeSort(arr, size):
    arrMerge = [0] * size
    mergesortUtil(arr, arrMerge, 0, size-1)

def mergesortUtil(arr, arrMerge, left, right):

    if left < right:
        mid = (left + right) // 2
        mergesortUtil(arr, arrMerge, left, mid)
        mergesortUtil(arr, arrMerge, mid+1, right)
        merge(arr, arrMerge, left, mid, right)

def merge(arr, arrMerge, left, mid, right):
    global swapCount
    index1 = left
    index2 = mid+1
    indexM = left

    for i in range(left, right+1):
        arrMerge[i] = arr[i]

    while index1 <= mid and index2<=right:
        # 그냥 병합정렬 문제는 등호가 상관 없지만 해당 문제에서는 등호에 따라 count수가 바뀜.
        # ex) 2, 2 -> 실제로 count 증가가 없는데 등호가 없다면 카운트가 증가하게 됨.
        if arrMerge[index1] <= arrMerge[index2]:
            # 오른쪽 배열에 있는 값을 저장할때, 왼쪽 배열에 남은 인덱스만 더하면 됨.
            # swapCount += right - index2 + 1
            arr[indexM] = arrMerge[index1]
            indexM += 1
            index1 += 1

        else:
            swapCount += mid - index1 + 1
            arr[indexM] = arrMerge[index2]
            indexM += 1
            index2 += 1

    while index1<=mid:
            arr[indexM] = arrMerge[index1]
            indexM += 1
            index1 += 1

    while index2<=right:
            arr[indexM] = arrMerge[index2]
            indexM += 1
            index2 += 1

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
swapCount = 0
mergeSort(a, n)
print(swapCount)