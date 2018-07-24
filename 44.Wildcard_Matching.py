class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = 'x' + s
        p = 'x' + p
        ns = len(s)
        np = len(p)
        
        dp = [[False]*ns for p in range(np)]
        
        dp[0][0] = True
        i = 1
        while i < np and p[i] == '*':
            dp[i][0] = True
            i += 1
            
        for i in range(1, np):
            for j in range(1, ns):
                if p[i] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif p[i] == '?' or p[i] == s[j]:
                    dp[i][j] = dp[i-1][j-1]
            if not any(dp[i]):
                return False
        return dp[-1][-1]
            
