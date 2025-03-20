import sys

input = sys.stdin.readline
N = int(input())
M = int(input())

arr = list(map(int,input().split()))
cnt = 0

# from itertools import combinations

# comb = combinations(arr, 2)
# for c in comb:
#     a, b = c
#     if a+b == M:
#         cnt += 1
# print(cnt)

for k in arr:
    if (M - k) in arr:
        cnt += 1
print(cnt//2)