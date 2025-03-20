import sys

input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int,input().split()))

left, right = 0, 0
tmp = arr[0]
cnt = 0
while left < N and right < N:
    if tmp == M:
        cnt += 1
        right += 1
        if right == N:
            break
        tmp += arr[right]
    elif tmp < M:
        right += 1
        if right == N:
            break
        tmp += arr[right]
    else:
        tmp -= arr[left]
        left += 1

print(cnt)
