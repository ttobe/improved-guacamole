dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, K = map(int, input().split())

arr = []
visted = [[-1] * N for i in range(N)]
from collections import deque

players = []

for i in range(N):
    in_tmp = []
    tmp = list(map(int, input().split()))
    for j in range(N):
        in_tmp.append([tmp[j]])
    arr.append(in_tmp)

for i in range(M):
    tmp = list(map(int, input().split()))
    # for gun
    tmp.append(0)
    # for score
    tmp.append(0)
    tmp[0] -= 1
    tmp[1] -= 1
    players.append(tmp)

def get_gun(nx, ny, player_num):
    # 내총 내려놓고
    arr[nx][ny].append(players[player_num][4])
    # 내 총은 사라지는걸 표현하기 위한 0
    players[player_num][4] = 0
    # 있는 총 중에서 가장 높은 총 챙기기
    max_gun = max(arr[nx][ny])
    players[player_num][4] = max_gun
    arr[nx][ny].remove(max_gun)
def lose(player_num):
    x, y, d, s, gun, score = players[player_num]
    # 내총 내려놓고
    arr[x][y].append(gun)
    # 내 총은 사라지는걸 표현하기 위한 0
    players[player_num][4] = 0
    # 방향 그대로 한칸 이동하는데
    nx = x + dx[d]
    ny = y + dy[d]
    
    # out of bound 거나 해당 자리에 사람이 있다면
    if (nx <= -1 or nx >= N or ny <=-1 or ny >= M) or (visted[nx][ny] != -1):
        # 3번만 돈다. 왜냐하면 4번 도는건 제 방향
        for i in range(3):
            d = (d + i) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            # 비어있으면 바로 끝
            if (visted[nx][ny] != -1):
                break
    # 이동함.
    players[player_num][0], players[player_num][1] = nx, ny
    # 내가 여기 있다.
    visted[nx][ny] = player_num
    # 총 있으면 획득
    get_gun(nx,ny, player_num)

def win(player_num):
    x, y, d, s, gun, score = players[player_num]

    get_gun(x, y, player_num)

def move(player_num):
    x, y, d, s, gun, score = players[player_num]

    nx = x + dx[d]
    ny = y + dy[d]
    
    # out of bound
    if nx <= -1 or nx >= N or ny <=-1 or ny >= M:
        d = (d + 2) % 4
        nx = x + dx[d]
        ny = y + dy[d]
    
    # player가 없다면
    if visted[nx][ny] == -1:
        # 내총 내려놓고 있는 총 중에서 가장 높은 총 챙기기
        get_gun()
        # 내가 여기 있다.
        visted[nx][ny] = player_num
        # 그 전의 곳은 없다.
        visted[x][y] = -1

    else:
        # player가 있다면, 있는 player가 visted에 번호가 들어가 있다.
        exist_player_num = visted[nx][ny]
        moved_s = s + gun
        exist_s = players[exist_player_num][3] + players[exist_player_num][4]

        if moved_s < exist_s:
            
            lose(player_num)
            win(exist_player_num)


    players[player_num][0], players[player_num][1] = nx, ny
    


for i in range(M):
    x, y = players[i][0], players[i][1]
    visted[x][y] = True


for _ in range(1):
    for i in range(M):
        move(i)

for i in range(N):
    print(arr[i])
print(players)