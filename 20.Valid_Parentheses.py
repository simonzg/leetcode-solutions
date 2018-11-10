class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if not stack:
                    return False
                pre = stack.pop()
                if pre+ch not in ['()','{}','[]']:
                    return False
        return not stack
