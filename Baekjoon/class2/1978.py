# 소수 찾기

N = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(N):
    tmp = 0
    for k in range(2, arr[i]):
        # print(k, arr[i])
        if arr[i] % k == 0:
            tmp = 1
            break
    if tmp == 1:
        continue
    if arr[i] == 1:
        continue
    # print(i)
    cnt += 1

print(cnt)