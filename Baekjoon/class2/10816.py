# 숫자 카드 2

N = int(input())
sang = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

def binary(start, end, find):
    if start > end:
        return 0
    m = (start + end)//2
    if find == sang[m]:
        return sang[start:end+1].count(find)
    elif find < sang[m]:
        return binary(start, m-1, find)
    else:
        return binary(m+1, end, find)

for i in arr2:
    print(sang.count(i),end=' ')

