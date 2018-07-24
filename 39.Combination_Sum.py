class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            return [[]]
        if target < min(candidates) or not candidates:
            return []

        i = 0
        ans = []
        while i < len(candidates):
            v = candidates[i]
            for r in self.combinationSum(candidates[i:], target-v):
                r.insert(0,v)
                ans.append(r)
            i+=1
        return ans
            
            
