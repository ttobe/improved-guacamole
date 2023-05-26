# N과 M 2
# N까지 M개의 수열
N, M = map(int, input().split())

def back(nowArr, k):
    if len(nowArr) >= M:
        for i in range(M):
            print(nowArr[i],end=' ')
        print()
        return
    else:
        for i in range(k, N+1):
            # print(i)
            if i not in nowArr:
                if nowArr[-1] > i:
                    break
                nowArr.append(i)
                back(nowArr, i)
                nowArr.pop()


for i in range(1, N+1):
    back([i], i)