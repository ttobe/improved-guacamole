def sol(arr, depth, M):

    if depth == M:
        print(*arr)
        return
    
    for i in range(arr[-1], N+1):
        sol(arr + [i], depth+1, M)

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

from itertools import permutations

comb = permutations(arr, M)

for c in comb:
    print(*list(c))