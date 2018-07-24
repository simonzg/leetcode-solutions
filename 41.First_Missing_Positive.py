class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 1
        numDict = {}
        
        m = max(nums)
        for i in nums:
            if i<=0:
                continue
            else:
                numDict[i] = True
                
        for d in range(m+1):
            if numDict.get(d+1, False) == False:
                return d+1
        
                
