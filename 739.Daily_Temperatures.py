class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0]*len(T)
        for i,n in enumerate(T):
            while stack and n > stack[-1][1]:
                j,v = stack.pop()
                res[j] = i-j
            stack.append((i,n))
        return res
