N, M = map(int, input().split(" "))
arr = []
for i in range(N):
    arr.append(input())
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

from collections import deque

queue = deque()
start = (0, 0)

for i in range(N):
    if "I" in arr[i]:
        start = (i, arr[i].index("I"))

queue.append(start)
visited = [[False] * M for i in range(N)]
cnt = 0
while queue:
    now = queue.popleft()
    if visited[now[0]][now[1]]:
        continue
    visited[now[0]][now[1]] = True
    if arr[now[0]][now[1]] == "P":
        cnt += 1
    
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        
        if arr[nx][ny] == "O" or arr[nx][ny] == "P":
            queue.append((nx,ny))
       
            
if cnt == 0:
    print("TT")
else:
    print(cnt)