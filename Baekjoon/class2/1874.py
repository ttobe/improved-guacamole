import sys 
n = int(sys.stdin.readline())

stack = []
index = 1
result = ""
for _ in range(n):
    now = int(sys.stdin.readline())
    
    while index <= now:
        result += "+\n"
        stack.append(index)
        index += 1
    
    if now == stack[-1]:
        result += "-\n"
        stack.pop()
    else:
        result = "NO"
        break
print(result)
