import sys

T = int(sys.stdin.readline())

def dif(a, b):
    result = 0
    for i in range(4):
        if a[i] != b[i]:
            result += 1
    return result

def check(a, b, c):
    return dif(a, b) + dif(b, c) + dif(a, c)

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(str, sys.stdin.readline().split()))
    # print(arr)
    result = 1e9
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                tmp = check(arr[i], arr[j], arr[k])
                if result > tmp:
                    result = tmp
            if result == 0:
                break
        if result == 0:
            break
    print(result)