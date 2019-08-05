from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def cleanFor(i):
            while queue and queue[0] <= i-k:
                queue.popleft()
            while queue and len(queue) > 0 and nums[i] > nums[queue[-1]]:
                queue.pop()

        queue = deque([])
        ans = []
        n = len(nums)
        for i in range(n):
            cleanFor(i)
            queue.append(i)
            ans.append(nums[queue[0]])
        return ans[k-1:]
