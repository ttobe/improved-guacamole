# 수 정렬하기 3

# N개의 수 오름차순으로 정렬.
# FAQ에 입력을 저장하지 말라고...?
# 10,000보다 작거나 같은 자연수

import sys
N = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)