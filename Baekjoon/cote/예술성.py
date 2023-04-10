N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

color = [[0] * N for i in range(N)]
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, group_num):
    cnt = 0
    
    queue = deque()
    queue.append((x, y))
    color[x][y] = group_num
    while queue:

        x, y = queue.popleft()
        cnt += 1
        # print(x, y)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= N or ny <=-1 or ny >= N:
                continue

            if color[nx][ny] == 0:
                if arr[x][y] == arr[nx][ny]:
                    color[nx][ny] = group_num
                    queue.append((nx, ny))

    
    return cnt, arr[x][y]

def grouping():
    result = []
    for i in range(N):
        for j in range(N):
            color[i][j] = 0

    group_num = 1
    for i in range(N):
        for j in range(N):
            if color[i][j] == 0:
                cnt, total = dfs(i, j, group_num)
                result.append((cnt, total, group_num))
                group_num += 1
    
    return result

def closer(group_num, group_len):
    result = [0] * group_len
    for i in range(N):
        for j in range(N):
            if color[i][j] == group_num:

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx <= -1 or nx >= N or ny <=-1 or ny >= N:
                        continue

                    result[color[nx][ny]-1] += 1
    return result
                    
def scoring(group_len):
    total_score = 0
    for i in range(group_len-1):
        result = closer(i+1, group_len)
        # print(i,)
        # print(result)
        for j in range(i+1, group_len):
            # print(i, j)
            tmp = (r[i][0] + r[j][0]) * r[i][1] * r[j][1] * result[j]
            if tmp != 0:
                # print(tmp, '=', r[i][0], r[j][0], r[i][1] , r[j][1] , result[j])
                total_score += tmp
    return total_score


next_arr = [
    [0] * N
    for _ in range(N)
]
def rotate_square(sx, sy, square_n):
    # 정사각형을 시계방향으로 90' 회전합니다.
    for x in range(sx, sx + square_n):
        for y in range(sy, sy + square_n):
            # Step 1. (sx, sy)를 (0, 0)으로 옮겨주는 변환을 진행합니다. 
            ox, oy = x - sx, y - sy
            # Step 2. 변환된 상태에서는 회전 이후의 좌표가 (x, y) -> (y, square_n - x - 1)가 됩니다.
            rx, ry = oy, square_n - ox - 1
            # Step 3. 다시 (sx, sy)를 더해줍니다.
            next_arr[rx + sx][ry + sy] = arr[x][y]
def rotate():
    # Step 1. next arr값을 초기화해줍니다.
    for i in range(N):
        for j in range(N):
            next_arr[i][j] = 0
    
    # Step 2. 회전을 진행합니다.
    
    # Step 2 - 1. 십자 모양에 대한 반시계 회전을 진행합니다.
    for i in range(N):
        for j in range(N):
            # Case 2 - 1. 세로줄에 대해서는 (i, j) -> (j, i)가 됩니다.
            if j == N // 2:
                next_arr[j][i] = arr[i][j]
            # Case 2 - 2. 가로줄에 대해서는 (i, j) -> (n - j - 1, i)가 됩니다.
            elif i == N // 2:
                next_arr[N - j - 1][i] = arr[i][j]

    # Step 2 - 2. 4개의 정사각형에 대해 시계 방향 회전을 진행합니다.
    sqaure_n = N // 2
    rotate_square(0, 0, sqaure_n)
    rotate_square(0, sqaure_n + 1, sqaure_n)
    rotate_square(sqaure_n + 1, 0, sqaure_n)
    rotate_square(sqaure_n + 1, sqaure_n + 1, sqaure_n)
    
    # Step 3. next arr값을 다시 옮겨줍니다.
    for i in range(N):
        for j in range(N):
            arr[i][j] = next_arr[i][j]

total_total = 0
for k in range(4):
    # for i in range(N):
    #     print(arr[i])
    
    r = grouping()
    tmp = scoring(len(r))
    # print(tmp)
    total_total += tmp
    rotate()

print(total_total)