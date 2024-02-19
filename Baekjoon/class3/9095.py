import sys

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())

    arr = [0] * 12

    arr[1] = 1
    arr[2] = 2
    arr[3] = 4

    for i in range(4, N+2):
        arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
    
    print(arr[N])