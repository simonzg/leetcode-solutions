class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []

        cur = 0
        ans = 0
        while cur < len(height):
            while stack and height[cur] > stack[-1][0]:
                val, index = stack.pop()
                if not stack:
                    break
                distance = cur - stack[-1][1] - 1  # notice the - 1 here
                bounded = min(height[cur], stack[-1][0]) - val
                ans += distance * bounded
            stack.append((height[cur], cur))
            cur += 1
        return ans
