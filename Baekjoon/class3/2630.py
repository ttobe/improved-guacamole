# 모두 같은 색인지 검증하기
def check(a, b, n):
    global cnt
    color = arr[a][b] # 첫 번째 색

    for i in range(a, a+n):
        for j in range(b, b+n):
            if color != arr[i][j]:
                return False
            
    if color == 0:
        cnt[0] += 1
    else:
        cnt[1] += 1
    return True

# 아니면 나누기
def sol(a, b, n):
    if not check(a, b, n):
        k = n // 2
        sol(a, b, k)
        sol(a, b + k, k)
        sol(a + k, b, k)
        sol(a + k, b + k, k)

N = int(input())

arr = []
global cnt
cnt = [0, 0]
for i in range(N):
    arr.append(list(map(int, input().split())))

        
sol(0, 0, N)
print(cnt[0])
print(cnt[1])