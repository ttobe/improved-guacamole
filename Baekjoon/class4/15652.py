def sol(arr, depth, M):

    if depth == M:
        print(*arr)
        return
    
    for i in range(arr[-1], N+1):
        sol(arr + [i], depth+1, M)

import sys

N, M = map(int, sys.stdin.readline().split())

for i in range(1, N+1):
    sol([i], 1, M)