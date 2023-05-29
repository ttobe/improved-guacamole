# n-queen

# N = int(input())
N = 4
arr = [[False for j in range(N)]for i in range(N)]
global result
result = 0

def isOkay(x, i):
    for k in range(x):
        if i == k or abs(x - k) == abs(i - k):
            return False
        
    return True

def nqueen(x):
    global result
    if x == N:
        result += 1
        return
    else:
        for i in range(N):
            # print(i)
            print(x , i)
            for l in range(N):
                print(arr[l])

            

            if isOkay(x, i):
                arr[x][i] = True
                nqueen(x+1)
                arr[x][i] = False

nqueen(0)


print(result)

