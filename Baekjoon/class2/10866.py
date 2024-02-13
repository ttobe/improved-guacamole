import sys 
N = int(sys.stdin.readline())

from collections import deque
queue = deque()

for i in range(N):
    line = sys.stdin.readline()
    
    if line.startswith("push_front"):
        queue.appendleft(int(line.split(" ")[1]))
    elif line.startswith("push_back "):
        queue.append(int(line.split(" ")[1]))
    else:
        match line.strip():
            case "front":
                if len(queue) == 0:
                    print(-1)
                else:
                    print(queue[0])
            case "back":
                if len(queue) == 0:
                    print(-1)
                else:
                    print(queue[-1])
            case "size":
                print(len(queue))
            case "empty":
                if len(queue) == 0:
                    print(1)
                else:
                    print(0)
            case "pop_front":
                if len(queue) == 0:
                    print(-1)
                else:
                    print(queue.popleft())
            case "pop_back":
                if len(queue) == 0:
                    print(-1)
                else:
                    print(queue.pop())
            
        
    