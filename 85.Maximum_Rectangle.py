# with the help of 84. Largest Rectangle in Histogram
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m,n = len(matrix), len(matrix[0])
        ans = 0
        values = [0] * n
        for i in range(m):
            for j in range(n):
                values[j] = values[j]+1 if matrix[i][j] == '1' else 0
            ans = max(ans, self.largestRectangle(values))
        return ans
    
    def largestRectangle(self, values):
        values.append(0)
        n = len(values)
        ans, stack = 0, [-1]
        for i in range(n):
            while values[i] < values[stack[-1]]:
                h = values[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        values.pop()
        return ans
                
            
