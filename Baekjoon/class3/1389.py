N, M = map(int, input().split(" "))

graph = {i:[] for i in range(1, N+1)}

for i in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
    
def fs(start, cost, kevin):
    
    for k in graph[start]:
        if kevin[k] > (cost + 1):
            kevin[k] = cost + 1
            fs(k, cost+1, kevin)

result = []

for i in range(1, N+1):
    kevin = [1e9] * (N+1)
    kevin[i] = 0
    fs(i, 0, kevin)
    result.append(sum(kevin[1:]))
    
print(result.index(min(result)) + 1)