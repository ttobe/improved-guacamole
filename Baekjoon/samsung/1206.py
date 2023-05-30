# 왼쪽과 오른쪽 열었을때 거리 2 이상의 공간이 확보될 때 조망권 확보
# 14 
# 0 0 3 5 2 4 9 0 6 4 0 6 0 0

for k in range(10):
    N = input()
    building = list(map(int, input().split()))
    cnt = 0
    for i in range(2, int(N)-2):
        # 처음부터 오른쪽 2개 높은게 있는지
        batch = building[i-2:i+3]
        if building[i] == max(batch):
            batch.pop(2)
            # print(batch)
            cnt += building[i] - max(batch)
    print("#{}".format(k), cnt)