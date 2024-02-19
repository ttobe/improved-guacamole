import sys

N, M = map(int, sys.stdin.readline().split(" "))

arr = list(map(int,input().split()))
for i in range(N-1):
    arr[i+1] += arr[i]
arr = [0] + arr

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    print(arr[b]-arr[a-1])
    