import sys
input = sys.stdin.readline
# print = sys.stdout.write

# 병합정렬
def mergesort(arr, size):
    # 이것 때문에 공간복잡도는 O(N)
    arrMerge = [0] * size
    mergesortUtil(arr, arrMerge, 0, size-1)

# 재귀로 리스트를 반씩 쪼개는 과정.
def mergesortUtil(arr, arrMerge, left, right):
    # left right 같아지기 전까지. -> 같아지면 원소 한개일 때이다.
    if left < right:
        # 정수 나눗셈을 위해 // 사용 (/만쓰면 float나올수도 있음)
        mid = (left + right) // 2
        mergesortUtil(arr, arrMerge, left, mid)
        mergesortUtil(arr, arrMerge, mid + 1, right)
        merge(arr, arrMerge, left, mid, right)

# arr에 있는 값을 임시로 arrMerge에 저장 및 비교하여 arr에 정렬하여 저장하기.
def merge(arr, arrMerge, left, mid, right):
    index1 = left
    index2 = mid + 1
    indexM = left

    # 배열 복사
    for i in range(left, right + 1):
        arrMerge[i] = arr[i]

    # left ~ mid = 왼쪽 배열 / mid+1 ~ right = 오른쪽 배열
    while(index1 <= mid and index2 <= right):
        if arrMerge[index1] < arrMerge[index2]:
            arr[indexM] = arrMerge[index1]
            indexM += 1
            index1 += 1

        else:
            arr[indexM] = arrMerge[index2]
            indexM += 1
            index2 += 1

    while index1 <= mid:
        arr[indexM] = arrMerge[index1]
        indexM += 1
        index1 += 1

    while index2 <= right:
        arr[indexM] = arrMerge[index2]
        indexM += 1
        index2 += 1


n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

mergesort(a, n)

for i in range(n):
    print(a[i])