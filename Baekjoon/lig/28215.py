from itertools import combinations

N, K = map(int, input().split())
homes = []
dists = [[0] * N for _ in range(N)]

for i in range(N):
    homes.append(list(map(int, input().split())))

def getDist(i, j):
    return abs(homes[i][0] - homes[j][0]) +  abs(homes[i][1] - homes[j][1]) 

    
INF  = float("INF")  
# 가장 먼 거리 구하기
def getMaxDist(bunker):
    result = 0
    for i in range(N):
        dist = INF
        # 벙커 중에 가까운 곳
        for j in bunker:
            tmp = getDist(i, j)
            dist = min(tmp, dist)
        # 가장 먼 곳 거리 업데이트 하기
        result = max(result, dist)
    return result
final = INF  
for c in combinations(range(N),K):
    final = min(final, getMaxDist(c))

print(final)