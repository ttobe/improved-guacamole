# 동전 0

N, K = map(int, input().split())

arr = []

for i in range(N):
    arr.append(int(input()))


cnt = 0

for i in reversed(range(N)):
    cnt += K // arr[i]
    K = K % arr[i]

print(cnt)