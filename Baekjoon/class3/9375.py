import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = {}
    for i in range(N):
        name, ty = sys.stdin.readline().strip().split(" ")
        if ty in arr:
            arr[ty] += 1
        else:
            arr[ty] = 1
    
    cnt = 1
    for i in arr:
        cnt *= (arr[i] + 1)
    
    print(cnt-1)