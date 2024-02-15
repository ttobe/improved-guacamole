import sys 

N, M, B = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
min_value = 256
max_value = 0
for i in range(N):
    if min_value > min(arr[i]):
        min_value = min(arr[i])
    
    if max_value < max(arr[i]):
        max_value = max(arr[i])
        
result_h = 0
result_time = 9999999999

for h in range(min_value, max_value+1):
    minus = 0
    plus = 0
    
    for i in range(N):
        for j in range(M):
            # 설정한 높이와 차이
            diff = h - arr[i][j]
            # 차이가 + 이면 놓아야 하는 블럭 수
            if diff > 0:
                plus += diff
            # 아니면 빼야하는 블럭 수
            else:
                minus += abs(diff)
                
    # 블럭 수 검사, 인벤 + 빼서 얻는 수가 놓아야 하는 것 보다 적으면 안되는 것
    if B + minus < plus:
        continue
    
    # 최소 시간를 구하고, 최소시간과 같으면 높이도 업데이트 해주기
    time = minus * 2 + plus
    if time <= result_time:
        result_time = time
        result_h = h
    
print(result_time, result_h)