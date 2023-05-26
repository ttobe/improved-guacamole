# 통계학
import math

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

# 산술 평균
mean = round(sum(arr) / len(arr))
print(mean)
# 중앙값
arr.sort()
print(arr[N//2])
# 최빈값
from collections import Counter
cnt = Counter(arr).most_common(2)
if N > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
# 범위
print(arr[-1]-arr[0])