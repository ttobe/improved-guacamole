# 수 찾기


N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
arr.sort()
# arr2.sort()

for k in range(M):
    result = 0
    tmp = arr2[k]
    i = 0
    j = N-1
    # print(tmp)
    while(i <= j):
        pivot = (i+j)//2
        # print(pivot)
        if tmp == arr[pivot]:
            result = 1
            # print('find')
            break
        
        if tmp > arr[pivot]:
            i = pivot + 1
        elif tmp < arr[pivot]:
            j = pivot - 1
    
    if result == 1:
        print('1')
    else:
        print('0')