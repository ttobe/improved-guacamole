def sol(arr, now, depth, M):

    if depth == M:
        print(*now)
        return
    
    for i in range(now[-1], N+1):
        sol(arr + [i], depth+1, M)

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

from itertools import permutations

comb = permutations(arr, M)
comb = list(set(comb))
comb.sort()
for c in comb:
    print(*list(c))