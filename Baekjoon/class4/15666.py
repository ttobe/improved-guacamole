def sol(arr, now, depth, M, l):

    if depth == M:
        print(*now)
        return
    idx = arr.index(now[-1])
    for i in range(idx, l):
        sol(arr, now + [arr[i]], depth+1, M, l)

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = list(set(arr))
arr.sort()

for i in range(len(arr)):
    sol(arr, [arr[i]], 1, M, len(arr))