# Solved with heap (sort)
# time complexity: O(N*logN)
# space complexity: O(N)
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for p in points:
            i, j = p
            dist = i**2+j**2
            heapq.heappush(heap, (dist, [i, j]))

        return [heapq.heappop(heap)[1] for i in range(K)]
