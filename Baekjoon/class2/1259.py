# 팰린드롬수

# 앞뒤로 봐도 1577

while(True):
    N = input()
    
    if N == '0':
        break
    result = 0
    for i in range(len(N)//2):
        j = len(N) - i - 1
        if N[i] != N[j]:
            result = 1
            break

    if result == 1:
        print('no')
    else:
        print('yes')