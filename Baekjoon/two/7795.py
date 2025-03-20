import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M= map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    left = 0
    right = 0
    cnt = 0

    while left < N and right < M:
        if A[left] > B[right]:
            cnt += M - right
            left += 1
        else:
            right += 1

    print(cnt)