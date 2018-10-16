class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=2:
            return max([0] + nums[:2])
        return max(self.robHouse(nums[1:]), self.robHouse(nums[:-1]))
    
    def robHouse(self, nums):
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for k in range(2, n):
            dp[k] = max(dp[k-2]+nums[k], dp[k-1])
        return dp[-1]
        