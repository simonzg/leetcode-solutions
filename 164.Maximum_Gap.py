'''
Radix Sort
REF: https://leetcode.com/problems/maximum-gap/discuss/50649/Simple-radix-sort-solution-in-python
'''
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0
        k = len(str(max(nums)))
        
        source = nums
        base, divider = 10,1
        for r in range(k):
            buckets = [[] for i in range(10)]
            
            
            for n in source:
                radix = n % base // divider
                buckets[radix].append(n)
            
            target = []
            for bucket in buckets:
                target.extend(bucket)
        
            source = target
            base *=10
            divider *= 10
        
        maxDiff = 0
        for i in range(1, len(source)):
            maxDiff = max(maxDiff, source[i] - source[i-1])
        
        return maxDiff
        

""" Trick
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(nums)
        d = [n[i]-n[i-1] for i in range(1,len(n))]
        return max(d) if d else 0
"""

