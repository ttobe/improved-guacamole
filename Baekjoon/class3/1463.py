import sys

N = int(sys.stdin.readline())

arr = [0] * (N + 1)

for i in range(2, N+1):
    # 이번 거는 저번거에 1을 더한 것 
    arr[i] = arr[i-1] + 1
    
    # 3으로 나눠지면 1뺀거랑 3나눈거에 횟수 추가한거랑 min
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)

print(arr[N])