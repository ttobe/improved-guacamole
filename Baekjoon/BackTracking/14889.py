# 스타트와 링크

N = int(input())

arr = [[0] * N for i in range(N)]

for i in range(N):
    tmp = list(map(int, input().split()))
    arr[i] = tmp

start = [0]
length = N//2

def cal():
    return 0
def finding(l):
    if l == length:
        cal()
    else:
        for i in range(start[-1], N - length):