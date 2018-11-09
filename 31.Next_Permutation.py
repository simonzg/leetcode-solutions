class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        index = -1
        while i>0:
            if nums[i-1] < nums[i]:
                index = i-1
                break
            i-=1
        
        if index >=0:
            minVal = sys.maxsize
            swapIndex = len(nums)
            for i in range(index+1, len(nums)):
                if nums[i] > nums[index] and nums[i] < minVal:
                    swapIndex = i

            tmp = nums[index]
            nums[index] = nums[swapIndex]
            nums[swapIndex] = tmp
        
        nums[:] = nums[:index+1] + list(reversed(nums[index+1:]))