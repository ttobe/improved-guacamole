import sys

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)
from collections import deque

queue = deque()
queue.append(1)

while queue:
    now = queue.popleft()
    for nxt in graph[now]:
        if parent[nxt] == 0:  
            parent[nxt] = now
            queue.append(nxt)
    

for i in range(2, len(parent)):
    print(parent[i])