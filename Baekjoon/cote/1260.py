# DFS와 BFS

from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


for i in range(1, N+1):
    graph[i][i] = 1



def BFS(x):
    visited = [False] * (N+1)
    queue = deque()
    queue.append(x)

    while queue:

        x = queue.popleft()
        
        if visited[x] == True:
            continue
        visited[x] = True
        print(x, end = ' ')
        for i in range(1,N+1):
            if graph[x][i] == 1:
                queue.append(i)


visited = [False] * (N+1)
st = []


def DFS(x):
    visited[x] = True
    print(x, end = ' ')
    for i in range(1,N+1):
        if graph[x][i] == 1:
            if visited[i] == False:
                DFS(i)
            
DFS(V)
print()
BFS(V)




        
            