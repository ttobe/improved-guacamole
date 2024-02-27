N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

start = (0, 0)

for i in range(N):
    if 2 in arr[i]:
        start = (i, arr[i].index(2))
        break

# print(start)

visitied = [[False] * M for i in range(N)]
result = [[1e9] * M for i in range(N)]
from collections import deque
result[start[0]][start[1]] = 0

def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:

        now = queue.popleft()
        if visitied[now[0]][now[1]]:
            continue
        visitied[now[0]][now[1]] = True
        now_value = result[now[0]][now[1]] + 1
        # print(now)
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if 1 == arr[nx][ny] and result[nx][ny] >= now_value and not visitied[nx][ny]:
            
                result[nx][ny] = now_value
                queue.append((nx,ny))


bfs(start)

for i in range(N):
    for j in range(M):
        if result[i][j] == 1e9:
            if arr[i][j] == 0:
                print(0, end=" ")
            else:
                print(-1, end=" ")
        else:
            print(result[i][j], end=" ")
    print()