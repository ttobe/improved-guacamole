import sys
from collections import deque
T = int(sys.stdin.readline())

def sol(arr, func):
    flag = True
    for i in range(len(func)):
        if func[i] == "R":
            flag = not flag
        else:
            if len(arr) == 0:
                return "error"
            else:
                if flag == True:
                    arr.popleft()
                else:
                    arr.pop()
    if not flag:
        arr.reverse()
    return list(arr)

for _ in range(T):
    func = sys.stdin.readline().strip()
    N = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()
    
    if N != 0:
        arr = deque(list((map(int, arr[1:-1].split(",")))))
    else:
        arr = []
    
    result = sol(arr,func)
    if result == "error":
        print(result)
    elif len(result) == 0:
        print("[]")
    else:
        print("[", end="")
        for i in range(len(result) - 1):
            print(result[i], end=",")
        print(str(result[-1]) + "]")