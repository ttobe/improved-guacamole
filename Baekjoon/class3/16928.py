N, M = map(int, input().split())

ladder = {}
snake = {}
for i in range(N):
    a, b = map(int, input().split())
    ladder[a] = b

for i in range(M):
    a, b = map(int, input().split())
    snake[a] = b


from collections import deque
dist = [0] * 101
visited = [False] * 101
queue = deque()
queue.append(1)
dist[1] = 0
visited[1] = True
while queue:
    x = queue.popleft()
    visited[x] = True
    for i in range(1, 7):
        nx = x+i
        if 0 < nx <= 100 and not visited[nx]:
            if nx in ladder.keys():
                nx = ladder[nx]
            if nx in snake.keys():
                nx = snake[nx]

            if not visited[nx]:
                queue.append(nx)
                visited[nx] = True
                dist[nx] = dist[x] + 1

print(dist[100])