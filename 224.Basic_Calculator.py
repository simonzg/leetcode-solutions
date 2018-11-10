class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num, sign = 0, 1
        res, stack = 0, []
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch in '+-':
                res += num*sign
                num = 0
                sign = 1 if ch=='+' else -1
            elif ch =='(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif ch == ')':
                res += num*sign
                res *= stack.pop()
                res += stack.pop()
                num, sign = 0, 1
        return res + num*sign