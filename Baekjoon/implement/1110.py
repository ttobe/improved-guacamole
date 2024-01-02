# 더하기 사이클

N = int(input())
tmp = str(N)
cnt = 1
while(cnt < 61):

    if len(tmp) == 1:
        tmp = '0' + tmp
    
    add = str(int(tmp[0]) + int(tmp[1]))
    result = tmp[-1] + add[-1]
    if int(result) == N:
        break
    cnt += 1
    tmp = result


print(cnt)