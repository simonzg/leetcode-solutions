class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        for i in range(n+1):
            dp.append(0)
        dp[0] = 1
        dp[1] = 1

        cnt = 0
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
