# 트리의 부모 찾기

N = int(input())

graph = [[0] * (N+1) for i in range(N+1)]

for i in range(1, N):
    a, b = map(int, input().split())

    graph[a][b] = 1
    graph[b][a] = 1
    graph[i][i] = 1

for i in range(1, N+1):
    print(graph[i][1:])

result = [0] * (N+1)
prev = 1

def dfs(now):
    for next in range(1, N+1):
        if graph[now][next] == 1:
            
            if result[next] == 0:
                result[next] = now
                dfs(next)

dfs(1)

for i in range(2,N+1):
    print(result[i])