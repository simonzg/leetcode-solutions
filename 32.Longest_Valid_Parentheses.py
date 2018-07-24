# solution with O(n) complexity
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for ch in s:
            if not stack or ch == '(':
                stack.append(ch)
                continue
            else:
                currSum = 0
                i = len(stack) - 1
                while stack:
                    prevCh = stack.pop()
                    if prevCh == '(': # pair
                        stack.append(currSum+2)
                        break
                    elif prevCh == ')': # conflict
                        stack.append(prevCh)
                        if currSum > 0:
                            stack.append(currSum)
                        stack.append(ch)
                        break
                    else: # numbers
                        currSum += prevCh
                if not stack and currSum > 0: # no match/conflict at all
                    stack = [currSum, ')']
                    
        currMax = 0
        finalMax = 0
        
        for ch in stack:
            if ch in ['(',')']:
                finalMax, currMax = max(finalMax, currMax), 0
                continue
            else:
                currMax += ch
        return max(finalMax, currMax)
                
