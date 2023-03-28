# 수 정렬하기 2
# 정수 정렬


import sys
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    tmp = int(sys.stdin.readline())
    arr.append(tmp)

arr.sort()

for i in range(N):
    print(arr[i])