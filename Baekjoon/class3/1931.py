N = int(input())

arr = []

for i in range(N):
    start, end = map(int, input().split(" "))
    arr.append((start,end))
    
arr.sort(key=lambda x:(x[1], x[0]))

result = 0
index = 0
for start, end in arr:
    if index <= start:
        result += 1
        index = end
        
print(result)
