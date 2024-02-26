import sys
N = int(sys.stdin.readline())

adj = []

for i in range(N):
    adj.append(list(map(int, sys.stdin.readline().split(" "))))
visited = [False] * N

def DFS(x):
    # 내 주위 모든 노드에 대해
    for i in range(N):
        if adj[x][i] == 1 and visited[i] == False:
                visited[i] = True
                DFS(i)
            # DFS가 끝나면 다음 연결 노드를 검사하기!

for i in range(N):
    visited = [False] * N
    DFS(i)
    for j in range(N):
        if visited[j] == True:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
