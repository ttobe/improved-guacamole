import sys 
input = sys.stdin.readline
import copy

N = int(input())

arr = list(map(int, input().split()))
DP = [[0] * 3 for i in range(2)]
minDP = [[0] * 3 for i in range(2)]
DP[0] = copy.deepcopy(arr)
minDP[0] = copy.deepcopy(arr)
flag = 0
for i in range(1, N):
    inp = list(map(int, input().split()))
    prev = flag
    flag = (flag+1)%2
    # J = 0
    DP[flag][0] = inp[0] + max(DP[prev][0], DP[prev][1])
    minDP[flag][0] = inp[0] + min(minDP[prev][0], minDP[prev][1])
    # J = 1
    DP[flag][1] = inp[1] + max(DP[prev][0], DP[prev][1], DP[prev][2])
    minDP[flag][1] = inp[1] + min(minDP[prev][0], minDP[prev][1], minDP[prev][2])
    # J = 2
    DP[flag][2] = inp[2] + max(DP[prev][2], DP[prev][1])
    minDP[flag][2] = inp[2] + min(minDP[prev][2], minDP[prev][1])

    
print(max(DP[flag]), min(minDP[flag]))