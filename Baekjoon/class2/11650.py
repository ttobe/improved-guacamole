# 좌표 정렬하기


import sys
N = int(sys.stdin.readline())

arr = []
for i in range(N):
    (x, y) = map(int, sys.stdin.readline().split())

    arr.append((x,y))
arr.sort()
for i in range(N):
    print(arr[i][0], arr[i][1])
