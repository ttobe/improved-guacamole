import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
M = int(input())

left, right = 0, N-1
cnt = 0
arr.sort()
while left < right:
    tmp = arr[left] + arr[right]
    if tmp == M:
        cnt += 1
        left += 1
    elif tmp < M:
        left += 1
    else:
        right -= 1

print(cnt)
