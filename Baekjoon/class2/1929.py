N, M = map(int, input().split(" "))
import math
# 개선된 소수 판별 함수
def is_prime_number(n):
    end = int(n**(1/2))+1
    for i in range(2, end):
        if n % i == 0:
            return False
    return True
for i in range(N, M+1):
    #1은 소수가 아니므로 제외
    if i == 1:
        continue
    if is_prime_number(i):
        print(i)