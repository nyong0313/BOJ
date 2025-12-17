# 평균적으로 퀵소트는 O(n)의 시간 복잡도를 가진다.
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 문제에서는 인덱스 1번부터 시작하기 때문에.
k -= 1

def quick_sort(a, start, end, k):
    if start >= end:
        return

    pivot = start

    i = start+1
    j = end

    while i<=j:
        while i <= end and a[i] <= a[pivot]:
            i += 1

        while j >= start and a[j] >= a[pivot]:
            j -= 1

        if i > j:
            # a[j], a[pivot] = a[pivot], a[j]
            temp = a[j]
            a[j] = a[pivot]
            a[pivot] = temp

        else:
            # a[i], a[j] = a[j], a[i]
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

    if j == k:
        print(a[j])
    elif j < k:
        quick_sort(a, j+1, end, k)
    else:
        quick_sort(a, start, j-1, k)

quick_sort(a, 0, n-1, k)



# import sys

# input = sys.stdin.readline
# N, K = map(int, input().split())
# A = list(map(int, input().split()))


# def quickSort(S, E, K):
#     global A
#     if S < E:
#         pivot = partition(S, E)
#         if pivot == K:  # K번째 수가 pivot이면 더이상 구할 필요 없음
#             return
#         elif K < pivot:  # K가 pivot보다 작으면 왼쪽 그룹만 정렬
#             quickSort(S, pivot - 1, K)
#         else:  # K가 pivot보다 크면 오른쪽 그룹만 정렬
#             quickSort(pivot + 1, E, K)


# def swap(i, j):
#     global A
#     temp = A[i]
#     A[i] = A[j]
#     A[j] = temp


# def partition(S, E):
#     global A

#     if S + 1 == E:
#         if A[S] > A[E]:
#             swap(S, E)
#         return E

#     M = (S + E) // 2
#     swap(S, M)
#     pivot = A[S]
#     i = S + 1
#     j = E
#     while i <= j:
#         while j >= S and pivot < A[j]:
#             j = j - 1
#         while  i <= E and pivot > A[i] :
#             i = i + 1
#         if i < j:
#             swap(i, j)
#             i = i + 1
#             j = j - 1
#         else:
#             break
#     # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
#     A[S] = A[j]
#     A[j] = pivot
#     return j


# quickSort(0, N - 1, K - 1)
# print(A[K - 1])