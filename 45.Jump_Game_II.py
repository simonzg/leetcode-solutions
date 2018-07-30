class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_max_reach, curr_max_reach = 0,0
        i, njump = 0, 0
        while last_max_reach < len(nums) - 1:
            while i<= last_max_reach:
                curr_max_reach = max(curr_max_reach, i+nums[i])
                i+=1
            last_max_reach = curr_max_reach
            njump+=1
        return njump
        
