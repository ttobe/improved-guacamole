# 미로 탐색
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

 
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:

        x, y = queue.popleft()
        

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue

            # print(nx, ny)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
   


bfs(0,0)
# print(graph)
print(graph[N-1][M-1])