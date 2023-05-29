# 랜선 자르기

K, N = map(int, input().split())

# N개의 랜선을 만들려는데 K개의 무작위 선들이 있다.
arr = []
for i in range(K):
    arr.append(int(input()))

# print(arr)

start = 1
end = max(arr)

while start <= end:
    m = (start + end) //2
    lines = 0
    for i in arr:
        lines += i // m
    
    if lines >= N:
        start = m + 1
    else:
        end = m-1


print (end)