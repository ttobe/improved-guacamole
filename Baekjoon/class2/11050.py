# 이항계수
# 이항계수 구하기
# 식 = nk = n-1 k-1 + n-1 k
# import numpy as np
N, K = map(int, input().split())
arr = [[0 for j in range(N+1)]for i in range(N+1)]

for i in range(N+1):
    arr[i][0] = 1
    arr[i][i] = 1
for i in range(1, N+1):
    for j in range(K+1):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

# print(np.array(arr))

print(arr[N][K])