class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = dict([[n,n] for n in nums])
        return [i for i in range(1,len(nums)+1) if i not in dic]
