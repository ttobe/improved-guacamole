# 체스판 다시 칠하기

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(input())
result = []
for i in range(N-7):
    for j in range(M-7):
        case1 = 0
        case2 = 0

        for k in range(i,i+8):
            for l in range(j,j+8):
                tmp = arr[k][l]
                if (k + l) % 2 == 0:
                    if tmp != 'B':
                        case1 += 1
                    if tmp != 'W':
                        case2 += 1
                else:
                    if tmp != 'W':
                        case1 += 1
                    if tmp != 'B':
                        case2 += 1
        result.append(case1)
        result.append(case2)


print(min(result))