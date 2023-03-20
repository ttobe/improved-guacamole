# 부녀회장이 될테야
# k층 n호에는 몇명이 살고있는가
# a층 b호에 살려면 a-1층 1 ~ b호까지

T = int(input())

for test_case in range(T):
    k = int(input())
    n = int(input())

    lists = [[0 for j in range(n+1) ]for i in range(k+1)]

    for i in range(1,n+1):
        lists[0][i] = i

    for i in range(1, k+1):
        for j in range(1, n+1):
            lists[i][j] = lists[i-1][j] + lists[i][j-1]


    print(lists[k][n])

