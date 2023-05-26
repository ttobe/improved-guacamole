# N과 M
# N까지 M개의 수열
N, M = map(int, input().split())

def back(nowArr):
    if len(nowArr) >= M:
        for i in range(M):
            print(nowArr[i],end=' ')
        print()
        return
    else:
        for i in range(1, N+1):
            # print(i)
            if i not in nowArr:
                nowArr.append(i)
                back(nowArr)
                nowArr.pop()
for i in range(1, N+1):
    back([i])