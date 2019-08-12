# DP with memorization
# time complexity: O(N^3) ?
# space complexity: O(K*N^2)


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        # dp[i,j,1] = dp[i,j,K] + sum(stones[i:j])
        # dp[i,j,m] = min(dp[i,mid,1]+dp[mid,j,m-1])
        # initial: dp[i,i,1] = 0
        # dp[i,i,m] = inf

        n = len(stones)
        inf = float('inf')
        memo = {}
        presum = [0]*(n+1)

        for i in range(n):
            presum[i+1] = presum[i] + stones[i]

        def dp(i, j, m):
            # early termination (if stones[i:j] can't be merged into one pile)
            if (j - i + 1 - m) % (K - 1):
                return inf
            if i == j:
                return 0 if m == 1 else inf
            if m == 1:
                ans = dp(i, j, K)+presum[j+1] - presum[i]
                memo[(i, j, m)] = ans
            if (i, j, m) in memo:
                return memo[(i, j, m)]
            minVal = inf
            for mid in range(i, j, K-1):
                minVal = min(minVal, dp(i, mid, 1)+dp(mid+1, j, m-1))
            memo[(i, j, m)] = minVal
            return minVal
        ans = dp(0, n-1, 1)
        return ans if ans < inf else -1
