class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        ans, stack = 0, [-1]
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        height.pop()
        return ans
