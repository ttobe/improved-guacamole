import heapq
import sys
from collections import deque
T = int(sys.stdin.readline())
def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True
for _ in range(T):
    min_heap = []
    max_heap = []
    nums = dict()
    N = int(sys.stdin.readline())
    for _ in range(N):
        id, num = sys.stdin.readline().strip().split()

        if id == "I":
            # 중복 삽입일 때
            if num in nums:
                nums[num] += 1
            # 처음 삽입일 때
            else:
                nums[num] = 1
                # min_heap에 추가
                heapq.heappush(min_heap, num)
                # max_heap에 추가
                heapq.heappush(max_heap, -num)
        else:
            # 큐가 비어있지 않을 때만
            if not isEmpty(nums.items()):
                # 최댓값을 제거
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[-max_heap[0]] -= 1
                # 최솟값을 제거
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