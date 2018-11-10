'''
REF: 
'''
class Solution:
    def findKthLargest(self, nums, k):
        q = sorted(nums[:k])
        for i in range(k, len(nums)):
            n = nums[i]
            
            if n<=q[0]:
                continue
            if n>=q[-1]:
                q.append(n)
                q = q[1:]
                continue
            for j in range(1, len(q)):
                if n < q[j]:
                    q.insert(j,n)
                    q = q[1:]
                    break
        return q[0]
"""
from random import randint
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(l, r):
            ri = randint(l, r)
            nums[r], nums[ri] = nums[ri], nums[r]
            for i, v in enumerate(nums[l: r+1], l):
                if v >= nums[r]:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            return l - 1
        
        l, r, k = 0, len(nums) - 1, k - 1
        while True:
            pos = partition(l, r)
            if pos < k:
                l = pos + 1
            elif pos > k:
                r = pos - 1
            else:
                return nums[pos]
"""
