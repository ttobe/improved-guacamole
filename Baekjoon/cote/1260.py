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


visited = [False] * (N+1)

# 재귀
def DFS(x):
    # 위치 방문 처리 후 출력
    visited[x] = True
    print(x, end = ' ')
    
    # 내 주위 모든 노드에 대해
    for i in range(1,N+1):
        if graph[x][i] == 1:
            # 방문 안한 곳이라면 거기 DFS를 시작해라
            if visited[i] == False:
                DFS(i)
            # DFS가 끝나면 다음 연결 노드를 검사하기!




from collections import deque

def BFS(x):
    visited = [False] * (N+1)
    queue = deque()
    # 시작점을 집어넣기
    queue.append(x)

    # queue가 빌때 까지,
    while queue:
        # 맨 앞 뽑아서
        x = queue.popleft()
        # 만약에 이미 방문한 곳이라면, pass
        if visited[x] == True:
            continue
        # 방문처리 후 출력
        visited[x] = True
        print(x, end = ' ')

        # 주위에 이제 다 돌면서 방문 요청하기
        for i in range(1,N+1):
            if graph[x][i] == 1:
                queue.append(i)
DFS(V)
print()
BFS(V)