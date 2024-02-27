N = int(input())
ans = abs(100 - N) # ++ or -- 로 이동할 경우 -> 최댓값
M = int(input())
arr = []
if M > 0:
    arr = list(map(str,input().split()))

for num in range(1000001): 
    for i in str(num):
        if i in arr: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - N))

print(ans) 