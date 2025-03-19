import sys
import heapq
def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True

T = int(sys.stdin.readline())


for _ in range(T):
    k = int(sys.stdin.readline())
    max_heap = []
    min_heap = []
    for _ in range(k):
        s, n = sys.stdin.readline().split(" ")
        n = int(n)
        nums = dict()


        if s == "I":
            # 중복 삽입일 때
            if n in nums:
                nums[n] += 1
            # 처음 삽입일 때
            else:
                nums[n] = 1
                heapq.heappush(max_heap, -n)
                heapq.heappush(min_heap, n)
            
        else:
            if len(max_heap) == 0:
                continue

            if n == 1:
                # 최대 값 삭제
                while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                    temp = -heapq.heappop(max_heap)
                    if temp in nums:
                        del(nums[temp])
                nums[-max_heap[0]] -= 1
            else:
                while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                    temp = heapq.heappop(min_heap)
                    if temp in nums:
                        del(nums[temp])
                nums[min_heap[0]] -= 1

    # 결과 출력           
    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])