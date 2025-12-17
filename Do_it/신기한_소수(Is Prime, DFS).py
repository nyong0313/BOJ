import sys, math
input = sys.stdin.readline
n = int(input())

def isPrime(num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def makePrime(a):
    if len(str(a)) == n:
        print(a)

    else:
        for i in range(1, 10, 2):
            result = a * 10 + i
            if isPrime(result):
                makePrime(result)

# 아래와 같은 코드를 작성했을때,
# n == 1일때 틀림.
# def makePrime(a):
#     for i in range(1, 10, 2):
#         result = a * 10 + i
#         if isPrime(result):
#             if len(str(result)) == n:
#                 print(result)
    
#             else:
#                 makePrime(result)

a = [2, 3, 5, 7]

for i in a:
    makePrime(i)