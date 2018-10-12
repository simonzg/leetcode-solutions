'''
Recursive with memorization
'''
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = {}

        def dfs(target):
            if not target:
                return ['']
            if target in memo:
                return memo[target]
            res = []
            for w in wordDict:
                if target.startswith(w):
                    res.extend([w if not tail else w+' '+tail for tail in dfs(target[len(w):])])
            memo[target] = res
            return res
            
        return dfs(s)
