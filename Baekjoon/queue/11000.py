import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = []

for i in range(N):
    s, t = map(int, input().split())
    arr.append((s, t))

arr.sort(key=lambda x: (x[0],x[1]))

hq = [arr[0][1]]
for i in range(1, N):
    if arr[i][0] >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq, arr[i][1])

print(len(hq))