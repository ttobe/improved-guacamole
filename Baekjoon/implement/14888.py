N = int(input())
A = list(map(int, input().split()))
cal = list(map(int, input().split()))

def sol(a, b, pm):
    if pm == 0:
        return a + b
    if pm == 1:
        return a - b
    if pm == 2:
        return a * b
    if pm == 3:
        return int(a / b)

global min_result, max_result

min_result = int(1e9)
max_result = int(-1e9)

def solution(now, index, cal):
    global min_result, max_result
    if index == N:
        max_result = max(max_result, now)
        min_result = min(min_result, now)
        return 
    else:
        for i in range(4):
            if cal[i] > 0:
                cal[i] -= 1
                solution(sol(now, A[index], i), index+1, cal)
                cal[i] += 1

solution(A[0], 1, cal)
print(max_result)
print(min_result)