# N과 M
# N까지 M개의 수열
N, M = map(int, input().split())


def back():
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            back()
            result.pop()
result = []
back()