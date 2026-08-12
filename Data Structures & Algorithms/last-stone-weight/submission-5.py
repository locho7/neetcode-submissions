import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if (-1 * x) < (-1 * y):
                heapq.heappush(stones, y - x)
            elif (-1 * x) > (-1 * y):
                heapq.heappush(stones, x - y)

        return -1 * stones[0] if stones else 0