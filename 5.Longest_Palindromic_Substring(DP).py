class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        ans = s[0]
        dp = [[False]*n for i in range(n)]

        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1] and len(ans) < 2:
                ans = s[i:i+2]

        for i in range(n-1):
            for j in range(i+1, n):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    w = s[i:j+1]
                    if len(w) > len(ans):
                        ans = w
        return ans
