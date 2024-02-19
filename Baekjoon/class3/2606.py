import sys

N = int(sys.stdin.readline())

M = int(sys.stdin.readline())

graph = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * (N+1)

from collections import deque
queue = deque()

cnt = 0
queue.append(1)
visited[1] = True
while queue:
    x = queue.popleft()
    
    for i in range(1, N+1):
        if graph[x][i] == 1 and visited[i] == False:
            queue.append(i)
            visited[i] = True
            cnt += 1
            

print(cnt)