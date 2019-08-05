class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lh = [0]*n
        rh = [0]*n
        lm = 0
        for i in range(n):
            lm = max(lm, height[i])
            lh[i] = lm

        rm = 0
        for i in range(n-1, -1, -1):
            rm = max(rm, height[i])
            rh[i] = rm

        ans = 0
        for i in range(n):
            water = min(lh[i], rh[i]) - height[i]
            ans += water

        return ans
