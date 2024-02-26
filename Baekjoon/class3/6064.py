T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    a, b  = 1, 1
    cnt = 1
    flag = False
    while x <= M * N: # 최대 범위
        if (x-y) % N == 0: # 나머지로 확인
            flag = True
            break
        x += M
    
    if flag:
        print(x)
    else:
        print(-1)