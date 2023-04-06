# 음료수 얼먹기

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
cnt = 0
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False

# print(arr)
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            cnt+=1
print(cnt)