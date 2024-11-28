import sys

# 입력값 처리
N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

global answer
answer = 0

from collections import deque
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * M for _ in range(N)]


def dfs(i, j, dsum, cnt):
    global answer
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        answer = max(answer, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 및 제거
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt+1)
            visited[ni][nj] = False
# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(i, j):
    global answer
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        answer = max(answer, tmp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        exce(i, j)
print(answer)