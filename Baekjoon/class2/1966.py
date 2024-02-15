import sys 
T = int(sys.stdin.readline())

from collections import deque

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split(" "))
    queue = deque(list(map(int, sys.stdin.readline().strip().split(" "))))
    cnt = 0

    while queue:
        now = queue[0]
        # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
        # 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다.
        if now < max(queue):
            queue.rotate(-1)
            
        # 그렇지 않다면 바로 인쇄를 한다. 
        else:
            queue.popleft()
            cnt += 1
            if M == 0:
                break
        
        if M == 0:
            M = len(queue) - 1
        else:
            M -= 1
                   
    print(cnt)
    
    