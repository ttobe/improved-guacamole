import sys

input = sys.stdin.readline
N = int(input())

left, right = 1, 1
sum = 1
result = 1

## 1, 2만 예외처리
if N == 1 or N == 2:
  print(1)
  sys.exit()

while right < N//2 + 2:
    # print(left, right, sum)
    if sum == N:
        result += 1
        right +=1
        sum += right
    elif sum > N:
        sum -= left
        left +=1
    else:
        right +=1
        sum += right

print(result)