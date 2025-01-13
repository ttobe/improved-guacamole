from collections import deque

def sol(A, B):
    queue = deque()
    queue.append((A, 0))
    while queue:
        
        now, depth = queue.popleft()
        if now == B:
            return depth
        
        if now * 2 <= B:
            queue.append((now * 2, depth + 1))
        
        if now * 10 + 1 <= B:
            queue.append((now * 10 + 1, depth + 1))

    return -2

import sys

A, B = map(int, sys.stdin.readline().split())

print(sol(A,B)+1)