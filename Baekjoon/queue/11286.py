# 우선순위 큐 절댓값 힙

import sys
import heapq

N = int(sys.stdin.readline())

h = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(h) > 0:
            print(heapq.heappop(h)[1])
        else:
            print("0")
    else:
        heapq.heappush(h, (abs(x), x))