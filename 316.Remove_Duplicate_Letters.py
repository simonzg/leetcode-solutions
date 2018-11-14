class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i,ch in enumerate(s):
            if ch not in stack:
                while stack and ch < stack[-1] and stack[-1] in s[i+1:]:
                    stack.pop()
                stack.append(ch)
        return ''.join(stack)
