import sys 
N = int(sys.stdin.readline())

stack = []

for i in range(N):
    line = sys.stdin.readline()
    
    if line.startswith("push"):
        stack.append(int(line.split(" ")[1]))
    else:
        match line.strip():
            case "top":
                if len(stack) == 0:
                    print(-1)
                else:
                    print(stack[-1])
            case "size":
                print(len(stack))
            case "empty":
                if len(stack) == 0:
                    print(1)
                else:
                    print(0)
            case "pop":
                if len(stack) == 0:
                    print(-1)
                else:
                    print(stack.pop())
            
        
    