import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

result = float('inf')
a, b = float('inf'), float('inf')
left, right = 0, N - 1


while left < right:
    if abs(arr[left] + arr[right]) < result:
        result = abs(arr[left] + arr[right])
        a, b = arr[left] ,arr[right]

    if arr[left] + arr[right] < 0:
        left += 1
    else:
        right -= 1

print(a, b)