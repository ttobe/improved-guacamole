# 미로탈출
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

cnt = 1

# 그 전거 +1을 하기

def bfs( x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]

print(bfs(0,0))