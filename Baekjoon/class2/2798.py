# 블랙잭

# 21이 안넘는 가장 큰 숫자
# N 장의 카드를 깔고, M이 넘지 않는 가장 최선의 수 3장

N, M = map(int,input().split())

# N개의 카드
cards = list(map(int, input().split()))
cards.sort()

result = 0

# 3장을 뽑을거, 작은 3부터 i j k이런식으로 옮겨가며 시도?
for i in range(N):
    tmp = 0
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = cards[i] + cards[j] + cards[k]
            # 넘으면 넘기기
            if tmp > M:
                continue
            elif result < tmp :
                result = tmp


print(result)