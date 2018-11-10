'''
REF: https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.

f(0) = nums[0]
f(1) = max(nums[0], nums[1])
f(k) = max( f(k-2)+nums[k], f(k-1) )
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        dp[0], df[1] = nums[0], max(nums[0], nums[1])

        for k in range(2, len(nums)):
            dp[k] = max(dp[k-2]+nums[k], dp[k-1])
        return dp[-1]
