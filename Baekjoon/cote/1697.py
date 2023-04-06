# 숨바꼭질
from collections import deque

limit = 100000
N, K = map(int, input().split())
visited = [False] * 100001
dx = [-1, 1]

def dfs(x):
    queue = deque()
    result = 0
    queue.append((x, result))
    
    while queue:
        
        x, r = queue.popleft()
        visited[x] = True
        r += 1
        for i in range(2):
            nx = x + dx[i]
            if nx > limit or nx <= -1:
                continue

            if visited[nx] == True:
                continue

            if nx == K:
                return r
            else:
                queue.append((nx, r))
        
        nx = x * 2
        if nx > limit:
            continue
        if visited[nx] == True:
            continue

        if nx == K:
            return r
        else:
            queue.append((nx, r))

 
r = dfs(N)

if N == K:
    r = 0

print(r)

