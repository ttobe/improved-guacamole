import sys
from collections import deque
input = sys.stdin.readline

def dslr(n):
    return [('D', (2 * n) % 10000), 
            ('S', (n - 1) % 10000), 
            ('L', n % 1000 * 10 + n // 1000), 
            ('R', n % 10 * 1000 + n // 10)]


T = int(input())  # 테스트 케이스 개수 입력
for _ in range(T):
    A, B = map(int, input().split())  # A와 B를 입력받음
    visited = [False for _ in range(10000)]  # 방문 여부를 저장할 리스트 초기화
    
    queue = deque()
    queue.append(("", A))

    while queue:
        now, num = queue.popleft()

        if num == B:
            print(now)
            break
        
        d = dslr(num)
        for next_letter, next_num in d:
            if not visited[next_num]:
                visited[next_num] = True
                queue.append((now+next_letter, next_num))
    
        