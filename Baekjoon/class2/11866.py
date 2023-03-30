# 요시푸스 문제 0
import queue
N, K = map(int, input().split())

q = queue.Queue()

for i in range(1, N+1):
    q.put(i)
arr = []
tmp = 1
while(True):
    if q.empty():
        break
    if tmp % K == 0:
        arr.append(q.get())
    else:
        q.put(q.get())
    tmp += 1

print('<', end='')
for i in range(N-1):
    print(arr[i], end=', ')
print(arr[N-1], end='')
print('>')
