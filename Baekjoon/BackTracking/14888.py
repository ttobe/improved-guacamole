# 연산자 끼워 넣기

N = int(input())
# 수
arr = list(map(int, input().split()))
# 연산자 
mid = list(map(int, input().split()))

def cal(a, m, b):
    if m == 0:
        return a + b
    elif m == 1:
        return a - b
    elif m == 2:
        return a * b
    else:
        if a < 0:
            return -(abs(a) // b)
        else:
            return a // b
result = []
def back(nowV, index):
    if index == N-1:
        result.append(nowV)
    else:
        # 연산자 고르기, 4가지 돌면서
        for j in range(4):
            # 0이 아니면 그거 ㄱㄱ
            if mid[j] > 0:
                mid[j] -= 1
                r = cal(nowV, j, arr[index+1])
                back(r, index+1)
                mid[j] += 1

back(arr[0], 0)

print(max(result))
print(min(result))