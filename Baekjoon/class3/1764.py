# 듣보잡

# 듣못 N, 보못 M,
import sys

N, M = map(int, input().split())

arr = set()

for i in range(N):
    arr.add(sys.stdin.readline().strip())

cnt = 0
arr2 = set()
for i in range(M):
    arr2.add(sys.stdin.readline().strip())

set3 = arr & arr2
set3 = sorted(set3)
print(len(set3))

for k in set3:
    print(k)