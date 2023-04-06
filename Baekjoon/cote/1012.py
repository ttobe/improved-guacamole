# 유기농 배추

from collections import deque
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:


        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <=-1 or ny >= M:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx, ny))

def bfs(x, y):
    st = []
    st.append((x,y))

    while len(st) != 0:
        x, y = st.pop()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <=-1 or ny >= M:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                st.append((nx, ny))




for _ in range(T):

    M, N, K = map(int, input().split())
    graph = [[0] * M for i in range(N)]
    visited = [[False] * M for i in range(N)]

    # print(graph)
    
    for k in range(K):
        a, b = map(int, input().split())
        # print(a, b)
        graph[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if visited[i][j] == False:
                    cnt +=1
                    bfs(i, j)
    print(cnt)
