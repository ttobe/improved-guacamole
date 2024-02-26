N = int(input())
M = int(input())
S = input()

PN = "IOI" + ("OI" * (N-1))

cnt = 0
index = 0
result = 0

while index < (M-1):
    if S[index:index+3] == 'IOI':
        cnt += 1
        index += 2
        if cnt == N:
            result += 1
            cnt -= 1
    else:
        index += 1
        cnt = 0

print(result)