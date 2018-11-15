class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = []
        maxLen = 0
        for token in input.split('\n'):
            count = token.count('\t')
            token = token.lstrip('\t')
            while len(stack) > count:
                stack.pop()

            if '.' in token:
                maxLen = max(maxLen, sum(stack)+len(token))
            else:
                stack.append(len(token)+1)
        return maxLen