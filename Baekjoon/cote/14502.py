# 연구소
from collections import deque
import copy
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))


result = 0

def bfs():
    test_map = copy.deepcopy(graph)
    queue = deque()
 
    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 2:
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <=-1 or ny >= M:
                continue

            if test_map[nx][ny] == 0:
                test_map[nx][ny] = 2
                queue.append((nx, ny))

    zero_count = 0
    for i in range(N):
        for j in range(M):
            if test_map[i][j] == 0:
                zero_count += 1

    global result  

    result = max(result, zero_count)


cnt = 0

def make_wall(count):
    if count == 3:
        # print('hi')
        bfs()
        return
    for i in range(N):
        for k in range(M):
            if graph[i][k] == 0:
                graph[i][k] = 1
                make_wall(count+1)
                graph[i][k] = 0           

make_wall(0)
print(result)