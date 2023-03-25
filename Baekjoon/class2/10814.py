# 나이순 정렬

# 나이와 이름, 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 오기

# 회원 수 N
N = int(input())

arr = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    tu = (age,name)
    arr.append(tu)
arr.sort(key=lambda x:x[0])

for i in range(N):
    print(arr[i][0], arr[i][1])