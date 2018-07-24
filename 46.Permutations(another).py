class Solution:
    def permute(self, nums):
        ans = [[]]
        for n in nums:
            ans = [ a[:i] +[n]+ a[i:] for a in ans for i in range(len(a)+1) ]
        return ans           
            
