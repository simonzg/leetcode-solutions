class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<r:
            ml = l+(r-l)//2
            mr = ml+1
            if nums[ml]>nums[mr]:
                r = ml
            else:
                l = mr
        return l
