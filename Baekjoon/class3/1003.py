import sys
T = int(sys.stdin.readline())
arr = [[0, 0] for _ in range(41)]

arr[0][0] = 1
arr[1][1] = 1

start = 2

for i in range(2, 41):
    arr[i][0] = arr[i-1][0] + arr[i-2][0] 
    arr[i][1] = arr[i-1][1] + arr[i-2][1]

for _ in range(T):
    N = int(sys.stdin.readline())
    print(arr[N][0], arr[N][1])