from itertools import *

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

def cal(team, arr):
    sum = 0
    per = list(permutations(team, 2))
    for k in per:
        a, b = k
        sum += arr[a][b]
    return sum

comb = list(combinations(range(N), N//2))
l = len(comb)//2

result = 1e9
for i in range(l):
    a = cal(comb[i], arr)
    b = cal(comb[len(comb) - i - 1], arr)

    if result > abs(a-b):
        result = abs(a-b)

print(result)