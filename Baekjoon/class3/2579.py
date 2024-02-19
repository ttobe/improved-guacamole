N = int(input())
stair = [0]*301
for i in range(N):
    stair[i]=int(input())

dp = [0] * 301
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = stair[2] + max(stair[0], stair[1])

for i in range(3, N):
    dp[i] = stair[i] + max(dp[i-3] + stair[i-1], dp[i-2])
    
print(dp[N-1])