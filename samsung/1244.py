# 교환성

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    line = list(input().split())
    bonus = list(map(int, line[0]))
    switch = int(line[1])
    # 바꿔야 하는 횟수
    for i in range(switch):
        # 이미 바꾼 앞자리를 제외 한 뒤
        bat = bonus[i:]
        # max index
        maxindex = len(bonus)-1
        # 이미 바꾼 앞자리 빼고까지 에서 max 검사해서 max index를 찾는데, 뒤에서 부터 찾기
        for j in range(len(bat)):
            if bonus[maxindex] < bonus[len(bonus)-1 - j]:
                maxindex = len(bonus)-1 - j
        print(maxindex, bonus[maxindex])
        
        tmp = bonus[i]
        bonus[i] = bonus[maxindex]
        bonus[maxindex] = tmp
        print(i, bonus)

    print("#{} {}".format(test_case, ''.join(map(str,bonus))))

    #78466 2
