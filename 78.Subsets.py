# recursive solution
# time complexity: O(N)


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute(i):
            if i == 0:
                return [[], [nums[0]]]
            prefixs = permute(i-1)
            addition = [p+[nums[i]] for p in prefixs]
            return prefixs+addition
        if not nums or len(nums) == 0:
            return []
        return permute(len(nums)-1)
