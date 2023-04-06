# 토마토

from collections import deque
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs():
    while st:
        x, y = st.popleft()
        now = graph[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <=-1 or ny >= M:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = now +1
                st.append((nx, ny))
            

M , N = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
st = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            # print(i, j)
            st.append((i,j))

dfs()

result = -1
cant = 0
m = 0

for i in range(N):
    # print(graph[i])
    if 0 in graph[i]:
        cant = 1
    m = max(graph[i])
    result = max(m , result)

if cant == 1:
    print('-1')
else:
    print(result-1)

