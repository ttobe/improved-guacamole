import heapq
import sys
h = []
N = int(sys.stdin.readline())

for i in range(N):
    K = int(sys.stdin.readline())
    
    if K == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h, -K)
        
        
