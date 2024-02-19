from queue import PriorityQueue
que = PriorityQueue()

import sys
N = int(sys.stdin.readline())

for i in range(N):
    k = int(sys.stdin.readline())
    if k == 0:
        if not que:
            print(0)
        else:
            print(que.get())
    else:
        que.put(k)