import sys

input = sys.stdin.readline
N, K = map(int,input().split())
arr = list(map(int,input().split()))

left, right = 0, K
tmp = sum(arr[:K])
results = [tmp]
while left < N and right < N:
    tmp -= arr[left]
    tmp += arr[right]
    left += 1
    right += 1
    results.append(tmp)

print(max(results))
