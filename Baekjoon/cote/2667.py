# 단지 번호 붙이기

from collections import deque

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


visted = [[False] * N for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 0
    # print('start bfs', x, y)
    while queue:

        x, y = queue.popleft()
        if visted[x][y] == True:
            continue

        visted[x][y] = True
        cnt += 1
        # print(x, y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                continue

            if visted[nx][ny] == True:
                continue

            queue.append((nx,ny))

    return cnt

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            continue
        
        if visted[i][j] == True:
            continue
        # print(i, j)
        result.append(bfs(i, j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])

