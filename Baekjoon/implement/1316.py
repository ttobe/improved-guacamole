# 그룹 단어 체커

N = int(input())

arr = []

for i in range(N):
    arr.append(input())

cnt = 0
for i in range(N):
    test_letter = arr[i][0]
    s = {test_letter}
    flag = True
    for j in range(1, len(arr[i])):
        if arr[i][j] == test_letter:
            continue
        if arr[i][j] in s:
            flag = False
            break
        test_letter = arr[i][j]
        s.add(arr[i][j])
    if flag:
        cnt += 1
print(cnt)