# 최대공약수와 최소공배수

a, b = map(int, input().split())

# 작은 수를 a로
if a > b:
    tmp = b
    b = a
    a = tmp

def gcd(a, b):
    while b > 0:
        a, b = b, a% b
    return a

def lcm(a, b):
    return a*b // gcd(a,b)
print(gcd(a,b))
print(lcm(a,b))