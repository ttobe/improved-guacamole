# Hashing
#가장 대표적인 방법은 항의 번호에 해당하는 만큼 특정한 숫자를 
# 거듭제곱해서 곱해준 다음 더하는 것이 있다.

r = 31
M = 1234567891

L = int(input())
s = input()

def alpha(x):
    return ord(x) - 96
result = 0
for i in range(L):
    result += alpha(s[i]) * pow(r, i)


print(result % M)