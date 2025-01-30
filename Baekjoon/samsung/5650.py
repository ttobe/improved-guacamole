# 핀볼 게임

import sys

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    graph = []
    warm = [[] for i in range(11)]
    starts = []
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            if line[j] >= 6:
                warm[line[j]].append((i, j))
            if line[j] == 0:
                starts.append((i, j))
        graph.append(line)
    # 게임판 위에서 출발 위치와 진행 방향을 임의로 선정가능 할 때,

    
