# 직각삼각형

while(True):
    # 인풋 받고 3개로 분리하기
    data = list(map(int, input().split()))
    
    # 세개가 0이면 끝
    if data[0] == 0 & data[1] == 0 & data[2] == 0:
        break
    
    data.sort()
    # 피타고라스
    if data[2]**2 == data[0] ** 2 + data[1] ** 2:
        print('right')
    else:
        print('wrong')