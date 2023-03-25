# 영화감독 숍

# 666이 들어가는 수 N번째 수



nth = 666
cnt = 0
N = int(input())
while True:
    if '666' in str(nth):
        cnt+=1 
                     #2 카운트를 올려라
    if cnt == N:          #4 카운트랑 n번째 수가 같다면 
        print(nth)           #5 nth를 출력하고
        break               #6 while문을 종료해라
    nth+=1 