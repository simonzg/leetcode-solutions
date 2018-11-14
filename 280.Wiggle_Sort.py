'''
REF: https://leetcode.com/problems/wiggle-sort/discuss/71693/My-explanations-of-the-best-voted-Algo
'''
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            if ((i&1==0) == (nums[i]>nums[i-1])):
                nums[i], nums[i-1] = nums[i-1], nums[i]
        
