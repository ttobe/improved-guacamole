# 바이러스

from collections import deque

computer_num = int(input())
connect = int(input())

graph = [[0] * (computer_num + 1) for i in range(computer_num+1)]

for i in range(connect):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, computer_num + 1):
    graph[i][i] = 1

visted = [False] * (computer_num + 1)

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:

        x = queue.popleft()
        visted[x] = True

        for i in range(1, computer_num+1):
            if graph[x][i] == 1:
                if visted[i] == False:
                    queue.append(i)

bfs(1)
# print(visted)
cnt = -1
for i in range(len(visted)):
    if visted[i]:
        cnt += 1

print(cnt)