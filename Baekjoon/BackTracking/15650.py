# N과 M 2
# N까지 M개의 수열
N, M = map(int, input().split())


def back(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    
    for i in range(start, N+1):
        if i not in result:
            result.append(i)
            back(i + 1)
            result.pop()
result = []
back(1)