class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        def dfs(prefix, l_remain, r_remain, res):
            if l_remain == 0 and r_remain == 0:
                res.append(prefix)
                return
            if l_remain>0:
                dfs(prefix+'(', l_remain-1, r_remain+1, res)
            
            if r_remain>0:
                dfs(prefix+')', l_remain, r_remain-1, res)
        
        dfs('', n, 0, res)
        return res