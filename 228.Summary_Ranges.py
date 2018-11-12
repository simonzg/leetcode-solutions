class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        for n in nums:
            if res and n == res[-1][-1]+1:
                res[-1].append(n)
            else:
                res.append([n])
        ans = []
        for r in res:
            if len(r) == 1:
                ans.append(str(r[0]))
            else:
                ans.append(str(r[0])+'->'+str(r[-1]))
        return ans
                
