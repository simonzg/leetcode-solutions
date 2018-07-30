# Insertion
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if not nums:
            return []
        nums = sorted(nums)
        ans, queue = [], [([], 0)]
        n = len(nums)
        while queue:
            prev, i = queue.pop(0)
            ans.append(prev)
            while i<n:
                v = nums[i]
                curr = prev+[v]
                queue.append((curr, i+1))
                while i<n and nums[i] == v:
                    i+=1
        return ans
            
        
