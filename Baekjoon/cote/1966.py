# 프린터 큐

# queue FIFO 
# 중요도 확인 후 높은 무ㄴ서가 있다면 뒤로 



T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    pointer = M
    cnt = 0
    while True:
        if max(arr) == arr[0]:
            # print(max(arr), arr[0], pointer)
            cnt += 1
            if pointer == 0:
                break
            else:
                pointer -= 1
            arr.pop(0)
        else:
            if pointer == 0:
                pointer = len(arr)-1
            else:
                pointer -= 1
            arr.append(arr[0])
            arr.pop(0)
            

        
    print(cnt)