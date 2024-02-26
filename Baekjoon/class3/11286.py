import heapq
import sys
q = []


N = int(input())

for i in range(N):
    k = int(sys.stdin.readline())
    if k is not 0:
        heapq.heappush(q, (abs(k), k))
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])