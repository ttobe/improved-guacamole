# 달팽이는 올라가고 싶다.

# A만큼 올라가지만 B만큼 미끄러진다.
# V 까지 올라가야함. 
import math

A, B, V = map(int, input().split())

day = A - B
cnt = 0

# 목적지에서 낮에 가는만큼 뺀 앞의 길이가 몇일만에 가는지
if (V-A) % day == 0:
    cnt = math.floor((V-A) / day) - 1
else:
    cnt = math.floor((V-A) / day) 

# 간만큼에서 낮에 V에 도달했으면 + 1
# 아님 2일이 걸린다는 소리니까 +2
if day * cnt + A >= V:
    cnt += 1
else:
    cnt += 2

print(cnt)