# ACM 호텔
# 정문에서 가장 짧은 방
# W개 H층
# H는 별로 상관 없고 W로 아래서부터
import math
T = int(input())

for test_case in range(T):

    H, W, N = map(int, input().split())
    
    floor = str(N % H)
    if floor == '0':
        floor = str(H)
    room = str(math.ceil(N / H))
    
    if len(room) == 1:
        room = '0' + room

    print(int(floor+room))