# 덩치덩치

# x kg, y cm 사람

# x > p & y > q 덩치가 더 크다
# N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 
# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.

N = int(input())
arr = []
rank = [1] * N

for i in range(N):
    tmp = tuple(map(int, input().split()))
    arr.append(tmp)

for i in range(N):
    for j in range(N):
        if arr[i][1] < arr[j][1] and arr[i][0] < arr[j][0]:
            rank[i] += 1


for i in range(N-1):
    print(rank[i], end=' ')
print(rank[N-1])