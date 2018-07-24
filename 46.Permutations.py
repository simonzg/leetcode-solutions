class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            comb = self.permute(nums[:i] + nums[i+1:])
            ans.extend([ [nums[i]]+c for c in comb])
        return ans
