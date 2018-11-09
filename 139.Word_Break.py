class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dic = {}
        for w in wordDict:
            dic.setdefault(w[0], []).append(w)
        
        memo = {}
        def dp(i):
            if i >= len(s):
                return True
            if i not in memo:
                if s[i] not in dic:
                    return False
                ans = []
                for w in dic[s[i]]:
                    n = len(w)
                    if s[i:i+n] == w:
                        ans.append(dp(i+n))
                memo[i] = any(ans)
            return memo[i]
        
        return dp(0)