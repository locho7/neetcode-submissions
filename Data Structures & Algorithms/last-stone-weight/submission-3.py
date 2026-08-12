import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * weight for weight in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            print(x, y)
            if (-1 * x) < (-1 * y):
                heapq.heappush(maxHeap, y - x)
            elif (-1 * x) > (-1 * y):
                heapq.heappush(maxHeap, x - y)
        print(maxHeap)

        return -1 * maxHeap[0] if maxHeap else 0