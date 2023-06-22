# 포켓몬..?

# 도감에 수록되어 있는 포켓몬 수 N
# 문제의 개수 M

# 입력: 포켓몬 이름 or 번호
import sys
N, M = map(int, input().split())

dict = {}

for i in range(1, N+1):
    tmp = sys.stdin.readline().strip()
    dict[i] = tmp
    dict[tmp] = i


# print(arr)
for _ in range(M):
    tmp = input()

    if tmp.isdigit():
        print(dict[int(tmp)])
    else:
        print(dict[tmp])
    

