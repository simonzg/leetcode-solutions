import sys
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        
        while l<r:
            m = (l+r)//2
            val = nums[m]
            if not ((nums[m] < nums[0]) == (target < nums[0])):
                val = -sys.maxsize if target < nums[0] else sys.maxsize
            if val < target:
                l = m+1
            elif val > target:
                r = m
            else:
                return m
        return -1
