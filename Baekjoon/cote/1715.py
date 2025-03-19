import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = []

for i in range(N):
    heapq.heappush(arr, int(input()))

result = 0

while len(arr) > 1:
    a = heapq.heappop(arr)
    a += heapq.heappop(arr)
    result += a
    heapq.heappush(arr, a)
print(result)