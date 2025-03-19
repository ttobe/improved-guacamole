N, M = map(int, input().split())
s = list(map(int, input().split()))

start = (s[0], s[1], s[2])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))


now_x, now_y, now_d = start
cnt = 0
while True:    
# for l in range(60):
    # 1. 현재가 청소되지 않은 경우 청소한다
    if arr[now_x][now_y] == 0:
        arr[now_x][now_y] = 2
        cnt += 1
    flag = False
    for i in range(4):
        now_d = (now_d + 3) % 4
        nx = now_x + dx[now_d]
        ny = now_y + dy[now_d]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if arr[nx][ny] == 0:
            now_x, now_y = nx, ny
            flag = True
            break

    if not flag:
        # back = (now_d + 2) % 4
        nx = now_x - dx[now_d]
        ny = now_y - dy[now_d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break
        if arr[nx][ny] == 1:
            break
        else:
            now_x, now_y = nx, ny


print( cnt)