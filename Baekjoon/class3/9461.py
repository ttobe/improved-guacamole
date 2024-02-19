import sys


arr = [0] * 101

arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2

T = int(sys.stdin.readline())

for _ in range(T):
    
    N = int(sys.stdin.readline())

    for i in range(6, N+1):
        arr[i] = arr[i-1] + arr[i-5]
    print(arr[N])