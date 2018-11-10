'''
Divide & Conquer
REF: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-solution-(divide-and-conquer).
'''
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i, ch in enumerate(input):
            if ch in '-+*':
                resLeft = self.diffWaysToCompute(input[:i])
                resRight = self.diffWaysToCompute(input[i+1:])
                for l in resLeft:
                    for r in resRight:
                        res.append(self.calc(l,r,ch))
        return res
    
    def calc(self, a,b, op):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        elif op == '*':
            return a*b
        else:
            return 0
