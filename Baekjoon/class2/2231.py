# 분해합

N = int(input())
result = 0
for i in range(N):
    tmp = 0
    # i 번째 각 자리수 다 더해보기
    for k in range(len(str(i))):
        tmp += int(str(i)[k])

    # 생성자라면
    if i + tmp == N:
        result = i
        break
    
print(result)

