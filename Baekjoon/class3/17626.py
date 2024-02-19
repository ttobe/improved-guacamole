import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1) 
dp[1] = 1

# 2 ~ N 까지
for i in range(2, N + 1):
    minimum = 1e9

    # 1부터 루트 i까지 
    for j in range(1, int(i ** 0.5) + 1):
        minimum = min(minimum, dp[i - (j ** 2)])
    dp[i] = minimum + 1

print(dp[N])