# 교환성

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    line = list(input().split())
    bonus = list(map(int, line[0]))
    switch = int(line[1])
    # 바꿔야 하는 횟수
    for i in range(switch):
        bat = bonus[i:]
        # 이미 바꾼 앞자리를 제외 한 뒤
        for k in range(len(bat)):
            m = bonus.index(max(bat))
            print("max bat", max(bat))
            print("bonus index", m)

            tmp = bonus[m]
            
            

            

        
        