# 비밀번호 찾기
import sys
N, M = map(int, input().split())

arr = {}

for i in range(N):
    site, pw = sys.stdin.readline().strip().split()

    arr[site] = pw

for i in range(M):
    site = sys.stdin.readline().strip()
    print(arr[site])