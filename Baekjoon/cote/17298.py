N = int(input())

arr = list(map(int, input().split(" ")))

NGE= [-1]*N
stack = [0] # 0번 인덱스

for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        NGE[stack.pop()] = arr[i]
    stack.append(i)
print(*NGE)
