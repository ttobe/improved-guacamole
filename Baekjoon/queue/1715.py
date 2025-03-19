import sys
import heapq

N = int(sys.stdin.readline())

h = []

for _ in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(h, x)

result = 0

while len(h) > 1:
    a = heapq.heappop(h)
    a += heapq.heappop(h)
    result += a
    heapq.heappush(h, a)

print(result)