N, M = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr)
while start <= end:
    m = (end + start) // 2
    
    # 잘린거 수 구하기
    tmp = sum([i - m for i in arr if i > m])
    # 잘린거가 M보다 작으면 end = M - 1 
    if tmp < M:
        end = m - 1
    else:
        start = m + 1

    
print(end)
    