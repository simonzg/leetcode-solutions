class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        seq = []
        max_len = 0
        for n in nums:
            if not seq or seq[-1]+1 == n:
                seq.append(n)
            elif seq[-1] != n:
                max_len = max(max_len, len(seq))
                seq = [n]
        return max(max_len, len(seq))
            
